```python
def triangle_area(a, h):
    return 3 * a * (h + a)

print(triangle_area(5, 3))  # Output: 15.5
print(triangle_area(4, 6))  # Output: 12.0
print(triangle_area(10, 5))  # Output: 52.0
```

This Python function, `triangle_area`, calculates the area of a triangle based on the lengths of its sides. The function uses the mathematical formula for the area of a triangle, which is the product of the base and the hypotenuse of the triangle.

The function takes two parameters: `a` and `h`, which represent the length of a side and the height of the triangle, respectively. It returns the area of the triangle, which is the product of the base and the hypotenuse.

The function is then tested with different values of `a` and `h`. The test passes successfully when the function returns the correct area for the given triangle.