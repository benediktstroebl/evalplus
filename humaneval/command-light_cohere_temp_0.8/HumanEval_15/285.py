```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}"
    
def test_string_sequence(test_case: int) -> None:
    """ Function to test the string_sequence function """
    assert len(string_sequence(test_case)) == 1 + test_case + 1, "Length of the string is not correct!"
    assert string_sequence(test_case).test_case) == "0 0 1 2 3 4 5", "String does not match the expected format!"
    return 

# Example test case
test_string_sequence(6)
```