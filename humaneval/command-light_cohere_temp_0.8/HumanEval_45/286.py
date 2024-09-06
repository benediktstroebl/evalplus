```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a * (h + a) / 2)

# Test the function with a set of test cases
if __name__ == "__main__":
    test_cases = [(2, 3), (5, 6), (8, 10)]
    for a, h in test_cases:
        print(f"Case {a} {h}: {triangle_area(a, h)}")
```
This code defines a function called `triangle_area` that calculates the area of a triangle based on the lengths of its sides. It also has a test cases to ensure the function's correctness.