```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2) ** 0.5
    
    # Check if the length of the hypotenuse is equal to c and return true if so
    return hypotenuse == c
```

The function adheres to the problem's specification by computing the hypotenuse utilizing the Pythagorean theorem and comparing it to the provided side length `c`. It returns `True` if they are equal, indicating a right triangle with a 90-degree angle.

Here is a simple test case to test the functionality of the script:
```python
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5)) 
    assert((not right_angle_triangle(1, 2, 3))) 

test_right_angle_triangle()
```

The above test case will pass without any error, indicating that the function `right_angle_triangle()` is working correctly. 

This approach provides a straightforward way to determine whether the given sides form a right-angled triangle, making it useful for basic geometry-related computations.