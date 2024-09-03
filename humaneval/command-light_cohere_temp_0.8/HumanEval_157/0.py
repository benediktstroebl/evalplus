```python
def right_angle_triangle(a, b, c):
    return a == b and b == c and c > 0 and a > 0 and a*c > b
def test_right_angle_triangle():
    assert right_angle_triangle(3,4,5) == True
    assert right_angle_triangle(1,2,3) == False
    assert right_angle_triangle(-1,2,3) == False
    assert right_angle_triangle(1,-2,3) == False
    assert right_angle_triangle(0,0,3) == True
    assert right_angle_triangle(2,0,1) == False
    assert right_angle_triangle(1,0,1) == True
```