# a3test.py
# Tech Kuo(thk42) and Charles Lai(cjl223)
# 10-8-2012
""" Unit Test for Assignment A3"""
import colormodel
import cunittest
import a3

def test_complement():
    """Test function complement"""
    cunittest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71), a3.complement_rgb(colormodel.RGB(250, 0, 71)))
    cunittest.assert_equals(colormodel.RGB(255-0, 255-0, 255-0), a3.complement_rgb(colormodel.RGB(0, 0, 0)))
    cunittest.assert_equals(colormodel.RGB(255-255, 255-255, 255-255), a3.complement_rgb(colormodel.RGB(255, 255, 255)))


def test_truncate5():
    """Test function truncate5"""
    cunittest.assert_equals("130.5",  a3.truncate5(130.59))
    cunittest.assert_equals("130.5",  a3.truncate5(130.54))
    cunittest.assert_equals("100.0",  a3.truncate5(100))
    cunittest.assert_equals("99.56",  a3.truncate5(99.566))
    cunittest.assert_equals("99.99",  a3.truncate5(99.99))
    cunittest.assert_equals("99.99",  a3.truncate5(99.995))
    cunittest.assert_equals("21.99",  a3.truncate5(21.99575))
    cunittest.assert_equals("21.99",  a3.truncate5(21.994))
    cunittest.assert_equals("10.01",  a3.truncate5(10.013567))
    cunittest.assert_equals("10.00",  a3.truncate5(10.000000005))
    cunittest.assert_equals("9.999",  a3.truncate5(9.9999))
    cunittest.assert_equals("9.999",  a3.truncate5(9.9993))
    cunittest.assert_equals("1.354",  a3.truncate5(1.3546))
    cunittest.assert_equals("1.354",  a3.truncate5(1.3544))
    cunittest.assert_equals("0.045",  a3.truncate5(.0456))
    cunittest.assert_equals("0.045",  a3.truncate5(.0453))
    cunittest.assert_equals("0.005",  a3.truncate5(.0056))
    cunittest.assert_equals("0.001",  a3.truncate5(.0013))
    cunittest.assert_equals("0.000",  a3.truncate5(.0004))
    cunittest.assert_equals("0.000",  a3.truncate5(.0009999))


def test_round5():
    """Test function round5"""
    cunittest.assert_equals("130.6",  a3.round5(130.59))
    cunittest.assert_equals("130.5",  a3.round5(130.54))
    cunittest.assert_equals("100.0",  a3.round5(100))
    cunittest.assert_equals("99.57",  a3.round5(99.566))
    cunittest.assert_equals("99.99",  a3.round5(99.99))
    cunittest.assert_equals("100.0",  a3.round5(99.9951))
    cunittest.assert_equals("22.00",  a3.round5(21.99575))
    cunittest.assert_equals("21.99",  a3.round5(21.994))
    cunittest.assert_equals("10.01",  a3.round5(10.013567))
    cunittest.assert_equals("10.00",  a3.round5(10.000000005))
    cunittest.assert_equals("10.00",  a3.round5(9.9999))
    cunittest.assert_equals("9.999",  a3.round5(9.9993))
    cunittest.assert_equals("1.355",  a3.round5(1.3546))
    cunittest.assert_equals("1.354",  a3.round5(1.3544))
    cunittest.assert_equals("0.046",  a3.round5(.0456))
    cunittest.assert_equals("0.045",  a3.round5(.0453))
    cunittest.assert_equals("0.006",  a3.round5(.0056))
    cunittest.assert_equals("0.001",  a3.round5(.0013))
    cunittest.assert_equals("0.000",  a3.round5(.0004))
    cunittest.assert_equals("0.001",  a3.round5(.0009999))


def test_to_strings():
    """Test toString methods"""
    cunittest.assert_equals("(30, 240, 230)",  a3.rgb_to_string(colormodel.RGB(30, 240, 230)));
    cunittest.assert_equals("(0, 0, 0)",  a3.rgb_to_string(colormodel.RGB(0, 0, 0)));
    cunittest.assert_equals("(255, 255, 255)",  a3.rgb_to_string(colormodel.RGB(255, 255, 255)));
    cunittest.assert_equals("(0.000, 0.000, 0.000, 0.000)",  a3.cmyk_to_string(colormodel.CMYK(0.0, 0.0, 0.0, 0.0)));
    cunittest.assert_equals("(100.0, 100.0, 100.0, 100.0)",  a3.cmyk_to_string(colormodel.CMYK(100.0, 100.0, 100.0, 100.0)));
    cunittest.assert_equals("(5.000, 56.50, 100.0, 11.60)",  a3.cmyk_to_string(colormodel.CMYK(5, 56.5, 100.00, 11.598)));
    cunittest.assert_equals("(359.9, 1.000, 1.000)",  a3.hsv_to_string(colormodel.HSV(359.9, 1.0, 1.0)));
    cunittest.assert_equals("(0.000, 0.000, 0.000)",  a3.hsv_to_string(colormodel.HSV(0.0, 0.0, 0.0)));
    cunittest.assert_equals("(157.0, 0.568, 0.400)",  a3.hsv_to_string(colormodel.HSV(157, .56789, .4)));


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cunittest.assert_equals("0.000", a3.round5(cmyk.cyan))
    cunittest.assert_equals("0.000", a3.round5(cmyk.magenta))
    cunittest.assert_equals("0.000", a3.round5(cmyk.yellow))
    cunittest.assert_equals("0.000", a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cunittest.assert_equals("0.000", a3.round5(cmyk.cyan))
    cunittest.assert_equals("0.000", a3.round5(cmyk.magenta))
    cunittest.assert_equals("0.000", a3.round5(cmyk.yellow))
    cunittest.assert_equals("100.0", a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cunittest.assert_equals("0.000", a3.round5(cmyk.cyan))
    cunittest.assert_equals("80.18", a3.round5(cmyk.magenta))
    cunittest.assert_equals("24.42", a3.round5(cmyk.yellow))
    cunittest.assert_equals("14.90", a3.round5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0.0, 0.0, 0.0, 0.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cunittest.assert_equals("255.0", a3.round5(rgb.red))
    cunittest.assert_equals("255.0", a3.round5(rgb.green))
    cunittest.assert_equals("255.0", a3.round5(rgb.blue))
    
    cmyk = colormodel.CMYK(0.0, 0.0, 0.0, 100.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cunittest.assert_equals("0.000", a3.round5(rgb.red))
    cunittest.assert_equals("0.000", a3.round5(rgb.green))
    cunittest.assert_equals("0.000", a3.round5(rgb.blue))
    
    cmyk = colormodel.CMYK(35.0, 80.18, 24.42, 14.90);
    rgb = a3.cmyk_to_rgb(cmyk);
    cunittest.assert_equals("141.0", a3.round5(rgb.red))
    cunittest.assert_equals("43.00", a3.round5(rgb.green))
    cunittest.assert_equals("164.0", a3.round5(rgb.blue))


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cunittest.assert_equals("0.000", a3.round5(hsv.hue))
    cunittest.assert_equals("0.000", a3.round5(hsv.saturation))
    cunittest.assert_equals("1.000", a3.round5(hsv.value))
    
    rgb = colormodel.RGB(0, 0, 0);
    hsv = a3.rgb_to_hsv(rgb)
    cunittest.assert_equals("0.000", a3.round5(hsv.hue))
    cunittest.assert_equals("0.000", a3.round5(hsv.saturation))
    cunittest.assert_equals("0.000", a3.round5(hsv.value))
    
    rgb = colormodel.RGB(217, 43, 164);
    hsv = a3.rgb_to_hsv(rgb);
    cunittest.assert_equals("318.3", a3.round5(hsv.hue))
    cunittest.assert_equals("0.802", a3.round5(hsv.saturation))
    cunittest.assert_equals("0.851", a3.round5(hsv.value))


def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    hsv = colormodel.HSV(0.0, 0.0, 0.0);
    rgb = a3.hsv_to_rgb(hsv);
    cunittest.assert_equals("0.000", a3.round5(rgb.red))
    cunittest.assert_equals("0.000", a3.round5(rgb.green))
    cunittest.assert_equals("0.000", a3.round5(rgb.blue))
    
    hsv = colormodel.HSV(0.0, 0.0, 1.0);
    rgb = a3.hsv_to_rgb(hsv);
    cunittest.assert_equals("255.0", a3.round5(rgb.red))
    cunittest.assert_equals("255.0", a3.round5(rgb.green))
    cunittest.assert_equals("255.0", a3.round5(rgb.blue))
    
    hsv = colormodel.HSV(217.9, 0.567, 0.23);
    rgb = a3.hsv_to_rgb(hsv);
    cunittest.assert_equals("25.00", a3.round5(rgb.red))
    cunittest.assert_equals("38.00", a3.round5(rgb.green))
    cunittest.assert_equals("59.00", a3.round5(rgb.blue))


# Application Code
if __name__ == "__main__":
    test_complement()
    test_truncate5()
    test_round5()
    test_to_strings()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
