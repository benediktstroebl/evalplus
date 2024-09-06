```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}" * (n + 1)

# Test cases
test_string_sequence = {
    "test_string_sequence":
    [
        "Should return the string '0 0 1 2 3 4 5' when n is 5?",
        None,
        "Should return the string with correct formatting for n = 0",
        "string_sequence(0)"
    ]
}

# Function Tests
test_string_sequence_func = {
    test_results = {}
    test_string_sequence_func()
    assert test_results["Should return the string '0 0 1 2 3 4 5' when n is 5?"] == True
    assert test_results["Should return the string with correct formatting for n = 0"] == True
    }
```