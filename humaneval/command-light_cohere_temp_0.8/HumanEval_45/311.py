```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a * (h + a)) / 2

# Test cases
tests = [
    (5, 3),
    (8, 6),
    (10, 5),
    (6, 7),
    (4, 8),
    (9, 2),
    (12, 1),
]

for case in tests:
    result = triangle_area(*case)
    assert result == pytest.6  # assert result == pytest.7.5