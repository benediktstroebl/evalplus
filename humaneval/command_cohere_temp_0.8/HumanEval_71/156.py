```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        try:
            area = (a * b * math.sqrt(3) / 2)
            return round(area, 2)
        except ValueError:
            return -1
    else:
        return -1
```

The function assesses the validity of the triangle using the principle that the sum of any two sides should be greater than the length of the third side. Once the triangle is validated, the function employs the Heronian formula to compute the area and rounds it to two decimal places before returning the result. If the lengths do not form a valid triangle, the function returns -1. 

This code can be copied and pasted into a Python environment to replicate and analyze the behavior of the function with various input lengths.