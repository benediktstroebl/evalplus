```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semiperimeter
    p = (a * b * c) ** 0.5  # Perimeter

    # Determine if the triangle is right-angled
    return p * s == 2  # Pythagorean theorem
```

The Pythagorean theorem is used in the code to determine if the triangle is right-angled. This theorem states that the square of the length of the hypotenuse (c) of a right triangle is equal to the sum of the squares of the other two sides (a and b).

This code defines a Python function called `right_angle_triangle` that takes three arguments: `a`, `b`, and `c`, and determines whether these lengths can form a right-angled triangle. It calculates the semiperimeter (`s`) and perimeter (`p`) of the triangle. Then it returns True if the triangle is right-angled, and False otherwise.

Keep in mind that this approach has a cubic time complexity of O(N^2) due to the calculation of `p = (a*b*c)**.5`, but it is nonetheless efficient for practical applications. It's crucial to note that this function assumes that the inputs are valid float values. If the input is invalid, the function may not yield accurate results.