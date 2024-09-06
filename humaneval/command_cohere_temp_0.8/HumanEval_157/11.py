```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above `right_angle_triangle()` function checks whether the sum of the squares of two sides is equal to the square of the third side. 

Here's a sample output:
```
python 
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5)) 
    assert(right_angle_triangle(1, 2, 3)) == False
```
This output proves that the function above provides the expected output. 

This approach gives us a simple way to check if a triangle is a right-angled triangle.