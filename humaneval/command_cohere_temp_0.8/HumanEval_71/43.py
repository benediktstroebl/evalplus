```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
    else:
        return -1
```

The function checks whether the sum of any two of the side lengths is greater than the third side. If this condition is met, the function calculates the area and rounds it to two decimal places, or returns -1 if the sides do not form a valid triangle. 

To validate the function, you can write tests similar to the example given in the problem statement, such as: 
 ```python
test_cases = [[3, 4, 5], [1, 2, 10], [0, 0, 0], [7, 11, 8], [5, 7, 12]]
expected_results = [6.00, -1, -1, -1, -1]

for i in range(len(test_cases)):
    assert triangle_area(*test_cases[i]) == expected_results[i]
``` 

This will ensure that the function appropriately solves for the area of valid triangles and returns -1 for non-triangle inputs.