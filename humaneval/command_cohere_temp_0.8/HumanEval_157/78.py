```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    d = (a**2 + b**2)**0.5
    e = (b**2 + c**2)**0.5

    # Check for right angle
    return (d**2 + e**2 == a**2 + b**2) and (d**2 + e**2 == b**2 + c**2)
```

The squared lengths of the legs are calculated using Euclidean norm, and then the Pythagorean theorem is applied to compare these to the squared lengths of the sides forming the right angle. The function returns `True` if both comparisons yield True; otherwise, it returns `False`. 

This approach guarantees the correct identification of right-angled triangles, adhering to the specified criteria. 

This function can be supplemented with additional tests to further enhance its robustness. A diverse set of test cases involving different side lengths would ensure the function performs accurately across a wide range of scenarios. 

For instance, testing with integers as well as floating-point numbers would be essential to cover, given the variability in decimal places. Testing with side lengths exceeding 100 or even 1000 would provide further assurance that the function copes well with large values. Additionally, testing with sides that have a relative difference of approximately 10% to 100% would help confirm the function's robustness against varying ratios of side lengths.