```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the length of a side and the height of the triangle, and it will return the area of the triangle. Test cases can be created to ensure its correctness:
```python
# Test case
assert triangle_area(5, 3) == 7.5
``` 
This way, you can ensure that the function performs as expected and produces the correct output.