```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Using the formula for the area of a triangle: base * height / 2
    return 0.5 * a * h
```

To test the function, add the following code after the function and before the script ends:
```python
assert triangle_area(5, 3) == 7.5, "Incorrect area calculation."
``` 
This will verify that the function produces the anticipated outcome.