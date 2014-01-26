# a3.py
# Tech Kuo (thk42) and Charles Lai (cjl223)
# 10-8-12
""" Functions for Assignment A3"""
import colormodel
import math

def complement_rgb(rgb):
   """Returns: the complement of color rgb.
   
   Precondition: rgb is an RGB object"""
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   return colormodel.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def truncate5(value):
   """Returns: value, as a string, using exactly 5 characters.

   The truncated value will have one of the forms:
      ddd.d      Example:  '360.1'
      dd.dd      Example:  '29.53'
      d.ddd      Examples: '4.003',  '0.001',  and '0.000'
   
   Precondition: value is a number (int or float), 0 <= value <= 999."""
   
   assert (type(value) == int or type(value) == float), 'Value '+ `value`+' is not a number'
   assert (0 <= value  and value <= 999), 'Value '+ `value`+' is outside of the range 0..999'
   value = float(value)
   if value<.001:
      value = 0.0
   value = str(value)+"00"
   return value[0:5]


def round5(value):
   """ Returns: value, as a string, but expanded or rounded to be (if necessary) exactly 5 characters.
   
   Examples:
      Round 1.3546  to  '1.355'.
      Round 1.3544  to  '1.354'.
      Round 21.9954 to  '22.00'.
      Round 21.994  to  '21.99'.
      Round 130.59  to  '130.6'.
      Round 130.54  to  '130.5'.
      Round 1       to  '1.000'.
   
   Precondition: value is a number (int or float), 0 <= value <= 360."""
   assert (type(value) == int or type(value) == float), 'Value '+ `value`+' is not a number'
   assert (0 <= value  and value <= 360), 'Value '+ `value`+' is outside of the range 0..360.'
   value = float(value)
   if value <10:
      value = round(value,3)
      value = truncate5(value)
      return value
   elif value>=10 and value<100:
      value = round(value,2)
      value = truncate5(value)
      return value
   else:
      value = round(value,1)
      value = truncate5(value)
      return value


def rgb_to_string(rgb):
   """Returns: String representation of rgb in the form "(R, G, B)".
   
   Precondition: rgb is an RGB object"""
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   return "("+`rgb.red`+","+" "+`rgb.green`+","+" "+`rgb.blue`+")"


def cmyk_to_string(cmyk):
   """Returns: String representation of cmyk in the form "(C, M, Y, K)".
   
   In the output, each of C, M, Y, and K should be exactly 5 characters long.
   
   Precondition: cmyk is an CMYK object."""
   assert (type(cmyk) == colormodel.CMYK), 'Value '+ `cmyk`+' is not a CMYK object'
   return "("+round5(cmyk.cyan)+", "+round5(cmyk.magenta)+", "+round5(cmyk.yellow)+", "+round5(cmyk.black)+")"


def hsv_to_string(hsv):
   """Returns: String representation of hsv in the form "(H, S, V)".
   
   In the output, each of H, S, and V should be exactly 5 characters long.
   
   Precondition: hsv is an HSV object."""
   assert (type(hsv) == colormodel.HSV), 'Value '+ `hsv`+' is not a HSV object'
   return "("+round5(hsv.hue)+", "+round5(hsv.saturation)+", "+round5(hsv.value)+")"


def rgb_to_cmyk(rgb):
   """Returns: color rgb as a CMYK object, with the most black possible.
   
   Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
   Precondition: rgb is an RGB object"""
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   R = (rgb.red/255.0)
   G = (rgb.green/255.0)
   B = (rgb.blue/255.0)
   Ci = 1 - R
   Mi = 1 - G
   Yi = 1 - B
   if Ci == 1 and Mi == 1 and Yi == 1:
      return colormodel.CMYK(0.0,0.0,0.0,100.0)
   else:
      K = min(Ci,Mi,Yi)
      C = ((Ci-K)/(1-K))*100.0
      M = ((Mi-K)/(1-K))*100.0
      Y = ((Yi-K)/(1-K))*100.0
      return colormodel.CMYK(C,M,Y,K*100.0)


def cmyk_to_rgb(cmyk):
   """Returns : color CMYK in as an RGB object.

   Formulae from en.wikipedia.org/wiki/CMYK_color_model.
   
   Precondition: cmyk is an CMYK object."""
   assert (type(cmyk) == colormodel.CMYK), 'Value '+ `cmyk`+' is not a CMYK object'
   C = (cmyk.cyan/100.0)
   M = (cmyk.magenta/100.0)
   Y = (cmyk.yellow/100.0)
   K = (cmyk.black/100.0)
   R = (1 - C)*(1 - K)
   G = (1 - M)*(1 - K)
   B = (1 - Y)*(1 - K)
   return colormodel.RGB(int(round(R*255)),int(round(G*255)),int(round(B*255)))


def rgb_to_hsv(rgb):
   """Return: color rgb as a HSV object.
   
   Formulae from wikipedia.org/wiki/HSV_color_space.
   
   Precondition: rgb is an RGB object"""
   assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
   r_h = (rgb.red/255.0)
   g_h = (rgb.green/255.0)
   b_h = (rgb.blue/255.0)
   MAX = max(r_h,g_h,b_h)
   MIN = min(r_h,g_h,b_h)
   if MAX == MIN:
      H = 0
   elif MAX == r_h and g_h>=b_h:
      H = 60.0 * (g_h - b_h) / (MAX - MIN)
   elif MAX == r_h and g_h < b_h:
      H = 60.0 * (g_h - b_h) / (MAX - MIN) + 360.0
   elif MAX == g_h:
      H = 60.0 * (b_h - r_h) / (MAX - MIN) + 120.0
   else:
      H = 60.0 * (r_h - g_h) / (MAX - MIN) + 240.0
   
   if MAX == 0:
      S = 0
   else:
      S = 1-MIN/MAX
   
   V = MAX
   
   return colormodel.HSV(H,S,V)


def hsv_to_rgb(hsv):
   """Returns: color hsv as an RGB object.
   
   Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
   
   Precondition: hsv is an HSV object."""
   assert (type(hsv) == colormodel.HSV), 'Value '+ `hsv`+' is not a HSV object'
   Hi = math.floor(hsv.hue/60)
   f = hsv.hue/60-Hi
   p = hsv.value*(1-hsv.saturation)
   q = hsv.value*(1-f*hsv.saturation)
   t = hsv.value*(1-(1-f)*hsv.saturation)
   
   if Hi == 0:
      R = hsv.value
      G = t
      B = p
   elif Hi == 1:
      R = q
      G = hsv.value
      B = p
   elif Hi == 2:
      R = p
      G = hsv.value
      B = t
   elif Hi == 3:
      R = p
      G = q
      B = hsv.value
   elif Hi == 4:
      R = t
      G = p
      B = hsv.value
   elif Hi == 5:
      R = hsv.value
      G = p
      B = q
   
   return colormodel.RGB(int(round(R*255)),int(round(G*255)),int(round(B*255)))