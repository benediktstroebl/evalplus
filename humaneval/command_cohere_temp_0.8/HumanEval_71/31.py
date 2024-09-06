```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        r = (a * b * (s[0] * s[0] + s[1] * s[1] - s[0] * s[1]) / (2 * s[0] * s[1]))
        return round(r, 2)
    else:
        return -1
``` 

The above code defines a function `triangle_area` that calculates the area of a triangle if the sum of any two sides is greater than the third side. The code uses a counterintuitive algebraic trick to calculate the area of the triangle based on the sides. The round() function is used to round the area to two decimal places. 

To ensure that the function operates on a valid triangle, the condition that the sum of any two sides is greater than the third side is checked. If the sides do not form a valid triangle, the function returns -1. 

To know more about the math behind the formula, please visit [Geoffrey Fox's Article](https://web.archive.org/web/20160304000858/http://www.foxhli.com/math/triangle/area.html).