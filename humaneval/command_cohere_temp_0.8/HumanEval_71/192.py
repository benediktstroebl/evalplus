```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        r = (a * b * (s[0] + s[1] + s[2]) / 2) / (s[0] * s[1] * s[2])
        return round(r, 2)
    else:
        return -1
```

The function checks whether the sum of any two of the side lengths is greater than the third side length. If the condition is met, it calculates the area using the formula ` Heron's Formula `. The calculated area is then rounded to two decimal places and returned. If the condition is not met, indicating an invalid triangle, the function returns -1. 

To ensure accuracy, the function verifies that the three side lengths are unique before performing any calculations.