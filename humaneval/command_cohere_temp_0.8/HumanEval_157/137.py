```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Determine if the triangle is right-angled
    if hypotenuse ** 2 == c ** 2 and hypotenuse ** 2 == a ** 2 + b ** 2:
        return True
    else:
        return False
```

The function `right_angle_triangle` leverages the Pythagorean theorem to calculate the length of the hypotenuse of the triangle. Subsequently, it compares the squared hypotenuse to the squared sum of the other two sides, which is a recognized method for determining whether a triangle is right-angled. The function returns 'True' if the triangle is right-angled and 'False' otherwise.

For robustness, the function can handle negative values for the triangle sides, but optimally it should be restricted to positive values to conform to the problem statement.

To ensure the function's correctness, it's crucial to thoroughly evaluate the inputs and ensure that the computed results align with the expected outcomes for myriad edge cases and values. This will help solidify its reliability and resilience as a solution to the problem.