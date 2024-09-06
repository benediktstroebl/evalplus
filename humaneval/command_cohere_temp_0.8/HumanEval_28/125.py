```python
# Importing the required module
from typing import List

# Defining the Concatenate function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Testing the function
if __name__ == "__main__":
    # Test Case 1: Empty list
    test_case1 = []
    print(f'Test Case 1: Expected "" | Got {concatenate(test_case1)}')
    assert concatenate(test_case1) == ""

    # Test Case 2: List with elements
    test_case2 = ["a", "b", "c"]
    print(f'Test Case 2: Expected "abc" | Got {concatenate(test_case2)}')
    assert concatenate(test_case2) == "abc"
```

This script includes a function called `concatenate`, which takes a list of strings as input and provides a single concatenated string as output. The function is tested twice, first with an empty list and then with a list containing three letters "a," "b," and "c." The tests verify that the function behaves correctly in both situations.