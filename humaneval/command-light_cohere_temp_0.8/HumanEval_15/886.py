```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_seq = [
    (0, "0"),
    (5, "050"),
    (10, "01000"),
    (12345, "123456"),
    (100000, "1000000")
]

# Loop through test cases and verify
for test in test_seq:
    actual = eval(test[0])
    expected = test[1]
    assert actual == expected, f"Verify {test}: actual={actual}, expected={expected}"
```