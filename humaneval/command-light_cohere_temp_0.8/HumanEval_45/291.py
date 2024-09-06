```python
def triangle_area(a, h):
    return 3 * (a * (h + a) / 2)

# Test case: Check if the function returns the correct area for a triangle with side length 5 and height 3
assert triangle_area(5, 3) == 7.5

# Test case: Check if the function raises an error when an invalid input is provided
try:
    triangle_area(-5, 3)
except TypeError:
    print("Function raised an error")

```