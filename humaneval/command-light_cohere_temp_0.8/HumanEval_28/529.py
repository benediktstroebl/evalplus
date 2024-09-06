```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)

# Test cases
test_cases = [
    [],  # Empty list
    ['a'],  # Single string
    ['a', 'b', 'c'],  # Three strings
    ['a', 'bcde', 'f'],  # More varied strings
    ]

for case in test_cases:
    actual = concatenate(case)
    print(f'Expected: "{actual}"')  # Print the expected output
``` 
This code defines a function called concatenate that takes a list of strings as input and returns the concatenated string. The output of the string is simply the list of strings joined without any extra separator.