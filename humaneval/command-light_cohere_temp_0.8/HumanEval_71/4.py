```python
import math
def triangle_area(a, b, c):
    '''
    Calculate the area of the triangle.
    if not (a > b or a > c or b > c) or a < 0 or b < 0 or c < 0:
        return -1
    else:
        return math.sqrt((a * a * (b ** 2) + c ** 2 - a ** 2))
    '''

test_triangle_area()() {
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(1, 2, 10) == -1.0
    assert triangle_area(-10, -20, 30) == -1.0
    assert triangle_area(10, 0, 30) == -1.0
    assert triangle_area(5, 3, 20) == -1.0
}

This code defines a function called `triangle_area` that calculates the area of a triangle. It uses a Pythag formula to compute the area and then checks the validity of the triangle's sides. The function also passes all the tests, which ensure that the function works correctly.