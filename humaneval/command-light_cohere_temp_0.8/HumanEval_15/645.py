```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_cases = [
    (0, ""),    # Base case
    (5, "0 5 10 15 20 25"), # Increasing value till n
    (1, "1"),    # Single number
    (12345, ""), # High value
    (0, "01234"), # Single leading zero
    (-5, "5"),    # Negative value
    ]

# Loop through test cases
for test_num, want in test_cases:
    actual = string_sequence(test_num)
    assert actual == want, f"Error in string generation for {test_num}"
```