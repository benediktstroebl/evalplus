```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Calculate the area using the formula: A = (1/2) * a * h
    area = 0.5 * a * h
    return area
```

To get the area of a triangle with side `a` and height `h` you can call this function with respective arguments as follows:
```python
area = triangle_area(5, 3)
print(area)  # Output: 7.5
```

This function returns the area of the triangle computed from the formula area = (1/2) * a * h. As seen from the example provided above, the function takes two arguments, `a` and `h`, representing the side and height of the triangle, respectively.