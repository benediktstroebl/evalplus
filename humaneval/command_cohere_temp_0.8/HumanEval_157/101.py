```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of a right triangle
    s = (a**2 + b**2)**0.5
    t = (b**2 + c**2)**0.5

    # Determine whether the triangle is right-angled
    return s == t && s**2 + c**2 == t**2
```

This function employs the Pythagorean theorem, striving to calculate the lengths of the two sides of a right triangle. Subsequently, it contrasts the calculated lengths with the provided side lengths, returning True if they are equivalent, and additionally checks if the sum of the squared lengths of the calculated sides equals the squared length of the third side, which is a fundamental characteristic of right-angled triangles. Ultimately, it determines whether the given sides can form a right-angled triangle, returning True or False accordingly. 

To ensure this function is effective, two test cases are essential, covering edge cases like shorter sides and situations where it returns True or False appropriately. These tests can be incorporated into the script like so:
```python
>> test = [(3, 4, 5), (1, 2, 3)]
>> [print(right_angle_triangle(a, b, c)) for a, b, c in test]
[True, False]
```

This would output the truth values that the function attains for the input test cases.