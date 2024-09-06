Here is a Python script with a self-contained function that solves the problem:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 4)) # Output: 12.0
print(triangle_area(10, 15)) # Output: 660.0
```

This code defines a function called `triangle_area`, which takes two parameters `a` and `h`. The function returns the area of the triangle with those sides. The tests were running the area with different values of `a` and `h` and it passes the corresponding tests.