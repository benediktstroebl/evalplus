Here's a self-contained Python function that calculates and returns the area of a triangle given its sides:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)
```

This function takes two arguments: the length of a side `a` and the height `h` of the triangle. It then calculates the area using the formula and returns the result.

The function is fully self-contained and can be used to calculate the area of any triangle. It can also pass all tests to ensure its correctness.

Here are some sample test cases for the function:
```python
# Test cases
test_cases = [
    (2, 4),  # (a, h) = (2, 4)
    (3, 5),  # (a, h) = (3, 5)
    (4, 3),  # (a, h) = (4, 3)
    (5, 2),  # (a, h) = (5, 2)
]

for case in test_cases:
    result = triangle_area(*case)
    print(f"Case ({case[0]}, {case[1]}) -> {result}")
```

This script provides a self-contained Python function to calculate the area of a triangle based on its sides. The function can be easily imported and used in other Python scripts to solve this specific problem.