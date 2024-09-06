```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total * total == a * a + b * b + c * c:
        return True
    else: 
        return False
```
This function calculates the sum of the squares of the three sides (total * total) and the sum of the squares of the two sides (a * a + b * b + c * c), it returns True if they are equal, and False otherwise.

Here is a simple test case to test the above function:
```python
test_cases = [[3, 4, 5], [1, 2, 3], [7, 7, 7]]

for i in test_cases:
    assert right_angle_triangle(*i)  == True
```

The above test cases can be extended to cover more scenarios to sufficiently validate the correctness of the `right_angle_triangle()` function.  This should help prove its correctness in a wide range of situations and validate its behavior in edge cases.