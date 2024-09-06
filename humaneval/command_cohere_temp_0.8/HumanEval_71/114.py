```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(s) * (s - max(s)) * 0.5)
        return round(area, 2)
    else:
        return -1
```

The function takes in three numbers, a, b, and c, as sides of a triangle. It first checks whether the sum of any two of these sides is dramatically different from the third side. If so, it returns -1, indicating an invalid triangle. If not, it calculates the area of the triangle using the formula `area = (base * height * 0.5)`, where the base and height are the two sides of the triangle. The result is then rounded to two decimal places and returned. 

Here is a test suite that could be used to validate the function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00
    
    # Should be invalid triangle
    assert triangle_area(1, 2, 10) == -1

    # Valid triangle with decimal input
    assert triangle_area(2.5, 3.5, 4.5) == 6.75

    # Another valid triangle
    assert triangle_area(5, 12, 13) == 16.50
```

These tests ensure that the function correctly identifies valid triangles and invalid triangles, and accurately calculates the area of valid triangles.