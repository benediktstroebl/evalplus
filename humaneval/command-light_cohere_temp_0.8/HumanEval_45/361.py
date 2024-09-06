```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a * (h + a) / 2)

# Test
assert triangle_area(5, 3) == 7.5, "Should be equal to the area of triangle with side lengths 5 and 3."

# This will fail without using assert, causing the script to fail on this line in development.
# Test again, it should be equal to the area of a triangle with side lengths 5 and 12.

# Test with a different set of numbers
assert triangle_area(8, 10) == 55.0, "Should be equal to the area of triangle with side lengths 8 and 10."
```