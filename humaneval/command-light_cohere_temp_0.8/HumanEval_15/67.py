```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n}{' ' * (n - 1)} {n + 1}"

# Test cases
test_seq = [
    "Does this function correctly generate string sequence starting from 0 ?",
    "it should closely match the output of string sequence(0)",
    assert string_sequence(0) == '0',
    "and for n = 5 ?",
    assert string_sequence(5) == '0 5 6 7 8'
]
test_seq()
```