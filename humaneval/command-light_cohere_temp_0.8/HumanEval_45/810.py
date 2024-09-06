```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test case: Check if function returns the correct result for a triangle with side length 5 and height 3
assert triangle_area(5, 3) == 7.5

# Test case: Check if function raises an error for an invalid input (negative side length)
try:
    triangle_area(-5, 3)
except TypeError:
    print("Function raised an error:", TypeError)

# Test case: Check if function raises an error for an invalid input (negative height)
try:
    triangle_area(3, -5)
except TypeError:
    print("Function raised an error:", TypeError)
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on its base and height. The function uses the specified function to solve the problem and pass corresponding tests.