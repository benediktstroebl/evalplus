```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
test_cases = [(5, 3), (6, 4), (8, 5)]

for a, h in test_cases:
    result = triangle_area(a, h)
    assert result == (a * (h + a) / 2), f"Failed for ( {a}, {h})"

print("All tests passed!")
```