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

The function checks whether the sides form a valid triangle first. If they do, it calculates the area and rounds it to 2 decimal places. Validation is done by checking that any two of the side lengths, when added together, are longer than the third side. The validation part of the function returns -1 if the triangle is not valid.

This solution assumes the input is valid decimal numbers. Lastly, this solution uses the Python `round()` function to round the area to two decimal places, and the `math.sqrt()` function to calculate the square root. Ensure that neither of these imports is missing in the environment where this solution is deployed.