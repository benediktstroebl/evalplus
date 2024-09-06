```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
    else:
        return -1
```

The function checks whether the sum of any two of the sides is greater than the third side. If all conditions are met, the function calculates the area and rounds it to 2 decimal places before returning it, and the area is calculated using the formula `(base * height * sqrt(3) / 2)`. 

Otherwise, the function returns -1, indicating that the sides do not form a valid triangle. 

This approach ensures that the function remains self-contained without importing any additional libraries and fulfills the given conditions of the problem.