```python
def triangle_area(a, h):
    return 5 * (h**2 + a**2)

# Test cases
test_cases = [(5, 3)]

for a, h in test_cases:
    result = triangle_area(a, h)
    print(f"Test case {a, h}: {result}")

```