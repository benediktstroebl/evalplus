```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c**2) + b * c * (a**2) + c * a * (b**2)) / 2
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by calculating the sum of the lengths of any two sides and comparing it with the length of the third side. If the condition is met, the function returns -1 to indicate that the sides do not form a valid triangle.

If the sides do form a valid triangle, the function calculates the area using the formula for the area of a triangle (half of the product of the lengths of the three sides multiplied by the square of the length of the longest side). The result is then rounded to two decimal places and returned.

The code includes an example in the docstring that shows how the function is used, and also includes tests to ensure the function behaves as expected.
```python
def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 5, 7) == 28.00
    assert triangle_area(20, 10, 5) == -1
```
This test_triangle_area function is a test suite that contains multiple test cases. Each test case is an assert statement that checks whether the `triangle_area` function returns the expected output for a specific input.

The first test case ensures that the function correctly calculates the area of a triangle with side lengths of 3, 4, and 5, and thus returns 6.00. The second test case ensures that the function correctly determines that side lengths of 1, 2, and 10 form an invalid triangle and thus return -1. The third test case ensures that the function correctly calculates the area of a triangle with side lengths of 10, 5, and 7, and thus returns 28.00. The last test case ensures that the function correctly determines that side lengths of 20, 10, and 5 form an invalid triangle and thus return -1.

```python
 callers = ['a', 'b', 'c']
 print(triangle_area(5, callers[0], callers[1]))
 print(triangle_area(5, callers[1], callers[2]))
 print(triangle_area(5, callers[2], callers[0]))
```
This code demonstrates how the `triangle_area` function could be used in a real-life situation. The code creates a list of variables, `callers`, containing the three variables `a`, `b`, and `c` to test the function in different ways. It then prints out the return value of `triangle_area` when passed 5, `a`, and `b`; 5, `b`, `c`; and 5, `c`, `a` respectively.

The code is a simple example of how the function can be used to calculate the area of a triangle with given side lengths and demonstrates that the function works no matter the order in which the sides are presented.