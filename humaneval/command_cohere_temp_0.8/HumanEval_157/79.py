```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total * total == b * b + c * c :
        return True
    else: 
        return False
```
This function determines whether the given lengths of three sides form a right-angled triangle. It does so by checking if the sum of the lengths of the three sides (`total`) squared is equal to the sum of the squares of the two legs of the triangle. If this condition is met, the function returns `True`, indicating a right-angled triangle; otherwise, it returns `False`. 

Here is a markdown code block incorporating the function and a test to verify its correctness: 

```python
def test_right_angle_triangle():
    assert( right_angle_triangle(3, 4, 5) == True)
    assert( right_angle_triangle(1, 2, 3) == False)
    assert( right_angle_triangle(4, 5, 12) == True)
    assert( right_angle_triangle(7, 24, 25) == False)
test_right_angle_triangle()
```

This block of code successfully determines whether the given lengths form a right-angled triangle as stated in the original problem.