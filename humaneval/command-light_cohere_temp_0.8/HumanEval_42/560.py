```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [
        0, 
        123, 
        0,
        10, 
        1234567, 
        0, 
        123456
    ]
]

for case, expected in test_incr_list:
    actual = incr_list(case)
    print(f"Case {case}: Expected {expected}, got {actual}")
```