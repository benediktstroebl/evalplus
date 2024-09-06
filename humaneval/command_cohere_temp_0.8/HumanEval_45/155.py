```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Using the formula for the area of a triangle: base * height / 2
    return 0.5 * a * h
```

To ensure that the function is self-contained and does not rely on external variables, it is defined with the necessary inputs (side length `a` and height `h`) and returns the calculated area. Additionally, the docstring provides a description of the problem, and the test case included verifies that the function correctly computes the area for a specific side length and height, making the function usable independently.  The `>`> marker denotes the test case that can be skipped. 

To run the test, you can add the following code after the function definition:
```python
>>> triangle_area(5, 3)
7.5
``` 
It is important to note that the test case is not a part of the function, but it is included in the script to verify correctness.