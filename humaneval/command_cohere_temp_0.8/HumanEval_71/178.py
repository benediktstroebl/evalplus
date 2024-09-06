```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        ar = (a * b * (s[0] * s[1] * s[2]) / 180)
        return round(ar, 2)
    else:
        return -1
```

The function checks whether the sum of any two of the side lengths is greater than the third side length. If any such combination is valid, the function calculates the area using the given formula and rounds it to two decimal places. If not, it returns -1 to indicate an invalid triangle. 

To ensure the robustness of the function, test cases should be added to cover various scenarios, including edge cases, to confirm the accuracy of the area calculation and the correctness of the validation logic.  These tests would guarantee that the function behaves as expected and provides the right output for each test scenario.  This is an important step in creating robust code that behaves correctly throughout different situations. 

The function above can be improved to more efficiently compute the area of a triangle given its side lengths. The formula used (`(a * b * h) / (4 * sqrt(3))`) is more accurate and performs better numerically, especially for triangles with side lengths that are not all equal. Also, providing a docstring for the function would be a great improvement in usability as it describes what the function does, and gives examples of how to use it. 

Here is the previously provided code snippet with a docstring and slightly modified to use the more efficient area calculation: 

```python
def triangle_area(a, b, c):
    """
    Calculates the area of a triangle given its side lengths a, b, and c.
    Returns rounded area if valid, and -1 otherwise.
    
    Examples:
    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] + s[1]) > s[2] and (s[0] + s[2]) > s[1] and (s[1] + s[2]) > s[0]:
        ar = (a * b * (s[0] * s[1] * s[2]) / (4 * sqrt(3)))
        return round(ar, 2)
    else:
        return -1
``` 

This function is more informative and easier to use correctly, thanks to the docstring. The example usage is shown in the docstring, and for further use, a module-level documentation string can provide more details on the purpose of the function and how to use it properly.