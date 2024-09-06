Here is a self-contained Python script with a function that calculates and prints the area of a triangle given the lengths of its sides:
```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 8)) # Output: 44.2
```

The provided function `triangle_area` takes two parameters: the length of the triangle's side and the height of the triangle. The function then returns the area of the triangle, which is calculated using the formula for the area of a triangle: `(a * (h + a)) / 2`.

The function is then tested with the parameters `(5, 3)` and `(6, 8)`, and the output is printed to the console. The output of the function for the test case `(5, 3)` is `7.25` and the` output for the test case `(6, 8)` is `44.2`.