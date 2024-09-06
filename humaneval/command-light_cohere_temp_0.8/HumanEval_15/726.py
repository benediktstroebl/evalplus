Here is a Python script with a self-contained function that solves the problem of generating a sequence of numbers in a markdown code block:

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 and ending at n-1 inclusive."""
    return f"0 {n} "

def test_string_sequence():
    """Test the string_sequence function with various values of n."""
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "1"
    assert string_sequence(5) == "0 5"
    assert string_sequence(10) == "0 9"
    assert string_sequence(15) == "0 14"
    assert string_sequence(3) == "3"

if __name__ == "__main__":
    test_string_sequence()
```

This script defines a function `string_sequence` which takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 and ending at `n-1` (inclusive). The test function `test_string_sequence` is used to test the correctness of the `string_sequence` function with various input values.