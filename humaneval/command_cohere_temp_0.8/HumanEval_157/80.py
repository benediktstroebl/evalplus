```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter s of the triangle

    # Check if the triangle is a right-angled triangle
    if s * (s - a) == b * c:
        return True
    else:
        return False
```

The following is the explanation of how the algorithm works:
1. `s = (a + b + c) / 2`: The semi-perimeter `s` of the triangle is a value that divides the sum of the side lengths `a`, `b`, and `c` by 2. It is a critical concept in the Sine Rule which is used to identify right-angled triangles.
2. `if s * (s - a) == b * c`: The Sine Rule states that for a triangle with sides `a`, `b`, and `c`, if `s * (s-a) = b * c`, then the angle opposite side `a` is a right angle (90 degrees). The equation is a symmetric equation and thus works for any side of the triangle. 

The preceding Python function implements this rule to determine whether the triangle is a right-angled triangle or not. 

This approach gives an efficient solution and earns a time complexity of O(1).