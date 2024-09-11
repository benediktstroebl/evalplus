```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    The formula for the area of a triangle is (base * height) / 2.
    In this case, the base is 'a' and the height is 'h'.
    
    :param a: Length of a side of the triangle.
    :type a: float
    :param h: Height of the triangle.
    :type h: float
    :return: Area of the triangle.
    :rtype: float
    """
    return (a * h) / 2

# Test the function
if __name__ == "__main__":
    print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of one side (`a`) and the height (`h`). The area is calculated using the formula `(base * height) / 2`, where the base is `a` and the height is `h`. 

In the `if __name__ == "__main__":` block, the function is tested with the example input `triangle_area(5, 3)`. The expected output is 7.5, which is printed to the console.