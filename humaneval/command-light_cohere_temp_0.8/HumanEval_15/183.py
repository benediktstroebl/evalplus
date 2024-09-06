```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 000{n+1}"

def test_string_sequence(test_case: int) -> None:
    n = test_case
    expected = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
    actual = string_sequence(n)
    assert actual == expected, f"Error in string sequence generation.
# Test cases
for i in range(1,6): test_string_sequence(i)
```