```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..."

def test_string_sequence(test_cases):
    """ Test function to check the working of string_sequence function."""
    for _ in range(test_cases):
        assert string_sequence(_) == f"0 {test_cases}..."
    return True

# Driver code
if __name__ == "__main__":
    test_cases = int(input())
    if test_cases:
        test_string_sequence(test_cases)
    else:
        print("No test cases passed")
```