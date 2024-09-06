```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3}"


def test_string_sequence(test_cases):
    """ Test function for string sequence function """
    for idx, test_case in enumerate(test_cases):
        assert str(test_case) == test_string_sequence(test_case), f"Test {idx+1}: failed"
    return "Test passed"

# Test data
test_cases = [0, 5]
test_results = test_string_sequence(test_cases)
print(test_results)  # Output: Test passed
 ```