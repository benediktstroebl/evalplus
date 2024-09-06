```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Calculate the area using the formula
    area = 0.5 * a * h
    return area
```

The function `triangle_area` takes in two parameters, `a` (side length) and `h` (height), and calculates the area of a triangle using the formula `Area = 1/2 * a * h`. The formula is inspired by the fact that the area of a triangle is equal to the product of half its base and height. The function then returns the calculated area. 

To see this in action let's use the function to calculate the area for a triangle with a side length of 5 and a height of 3:
```python
area = triangle_area(5, 3)
print(area)  # Output: 7.5
```

This demonstrates how the function can be used to determine the area of a triangle given a side length and height, confirming the accuracy of the formula used.