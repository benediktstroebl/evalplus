```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Function that XOR two strings """
    # Initialize empty result string
    result = ""

    # Append first character to result
    result += a[0]

    # XOR with second character
    result += b[0]

    # Append second to result
    result += a[1]

    # XOR with second character
    result += b[1]

    return result
test_cases = [
    "010", "110", "100", # Different combinations of strings
    "000", "001", "011", # Same strings
    # Different combinations of different characters
    "1010", "0110", "110",  # Different combinations of characters
    "0000", "1111", "1010", # Same strings with different order
]

# Function to test the string_xor function
def test(func, test_case):
    expected = test_case
    result = func(test_case)
    assert expected == result, f"Expected: {expected}, Got: {result}"

# Apply the function to all test cases
for test_case in test_cases:
    test(string_xor, test_case)
```