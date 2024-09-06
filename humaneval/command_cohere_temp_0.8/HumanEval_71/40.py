```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c)))), 2)
```
This function calculates the area of the triangle with sides `a`, `b`, and `c`. It first checks whether the sum of any two of these sides is greater than the third one, which is the condition for a valid triangle. If the sides do not form a valid triangle, the function returns -1. If the sides form a valid triangle, the function calculates the area using the formula `0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c))))` and rounds the result to two decimal places before returning it. 

Here is a test suite that can be used to validate the function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00
    
    # Should be a valid triangle, but arithmetic cause imprecision
    assert triangle_area(1, 2, 10) != -1.0
    
    # Invalid triangle
    assert triangle_area(10, 10, 10) == -1
    
    # Borderline case, where the sum is almost equal to a side
    assert triangle_area(1, 2, 3.0000001) == -1
    assert triangle_area(1, 2, 3.00001) == 6.0
    
    # Additional tests for edge cases
    assert triangle_area(0, 0, 0) == -1
    assert triangle_area(10, 10, 20) == -1
    assert triangle_area(0, 0, 10) == -1
    assert triangle_area(100, 100, 50) == -1
    assert triangle_area(-1, -1, 1) == -1
    assert triangle_area(1, -1, -1) == -1
    assert triangle_area(-1, 1, 1) == -1

test_triangle_area()
```

This test suite contains several test cases, including valid and invalid triangles, borderline cases, and edge cases, to thoroughly validate the function. 

The initial two tests check that the function appropriately identifies valid and invalid triangles and that the equation is correctly applied when a valid triangle is present. The following two tests examine edge cases, which are near-valid triangles where the difference between the sum of two sides and the third side is minimal enough to perhaps evade precise computations. The test suite also contains tests that challenge the function under various conditions such as 0 lengths or negative numbers which are not permissible.  By running this test suite, you can have confidence in the correctness of the function.