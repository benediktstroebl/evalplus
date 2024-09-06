```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. This solution makes use of list comprehension, and the pattern `s for s in strings if <condition>` is a concise way of filtering lists. The conditional `if` statement is used to iterate over each element of the list `strings` and include elements where the `substring` is present in the string. 

The function is designed to be self-contained, meaning it does not rely on external modules or assumptions, and it is easy to understand, as it closely resembles the problem description. 

To verify the functionality of this function, you can run the following tests:
```python
# Test with an empty list
test_list = []
test_substring = "abc"
result = filter_by_substring(test_list, test_substring)
assert result == []

# Test with valid inputs
test_list = ["abc", "bacd", "cde", "array"]
test_substring = "a"
result = filter_by_substring(test_list, test_substring)
assert result == ["abc", "bacd", "array"]

# Test with a substring that may occur multiple times
test_list = ["ababc", "bacd", "cde", "array"]
test_substring = "ab"
result = filter_by_substring(test_list, test_substring)
assert result == ["ababc", "bacd"]
```

These tests cover multiple scenarios, including the input being an empty list, a list with strings containing the substring at different positions, and ensuring that the resulting list correctly filters out the desired strings.  The `assert` statement ensures that the test performs as expected, returning an appropriate message if it does not. 
If you encounter any issues or challenges in understanding or running the code, feel free to ask for assistance.