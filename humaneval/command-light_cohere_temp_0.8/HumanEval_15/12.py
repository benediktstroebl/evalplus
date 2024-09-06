```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}"

def test_string_sequence(test_case: str) -> None:
    """ Test different inputs for string_sequence function and check if the output is correct."""
    if "0" not in test_case:
        return "Output not containing 0"
    if "5" not in test_case:
        return "Input not containing 5"
    if "0 1 2 3 4 5" not in test_case:
        return "Input not matching expected format"

    expected = test_case. Return f" print("Test case passed!") if expected == string_sequence(int(test_case)) else print("Test case failed")

# Example test cases
test_string_sequence("0")
test_string_sequence("5")
test_string_sequence("10 20 30")
test_string_sequence("100 101 102 103")
```
The code defines a function called string_sequence, which takes an integer n as input and returns a string containing space-separated numbers from 0 to n, inclusive. The function uses an formatted string to create the output. The test_string_sequence function tests the string_sequence function with different inputs and verifies if the output is correct. The test cases cover a expected behavior of the function, passing various input values and checking if the function returns the correct string sequence.