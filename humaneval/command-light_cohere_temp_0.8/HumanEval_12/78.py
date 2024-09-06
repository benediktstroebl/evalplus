```python
from typing import List
def longest(strings: List[str]):
    """ Outlines the list of strings, returns the length of the longest one.

    if not strings:
        return None

    max_len = 0
    longest_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string
    return longest_str if longest_str == "" else longest_len

# Test cases
strings = ["a", "b", "c"]
print(longest(strings))  # Output: cca
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: ccc
strings = []
print(longest(strings))  # Output: None
strings = ["abc", "abcd"]
print(longest(strings))  # Output: abcd
```

The provided Python script defines a function `longest` that takes a list of strings as input. It then iterates over the goal to find the longest string in the list. The script has a following logic:
1. First, it checks if the input list is empty. If the list is empty, it returns None.
2. If the list is not empty, it initializes a `max_len` variable to zero and a `longest_str` variable to an empty string.
3. Then, it iterates over each string in the list and checks the length of the string with the current `max_len`. If the length of the string is greater than `max_len`, it updates `max_len` and `longest_str` with the current string.
4. Finally, it returns `longest_str` variable if it's still empty after iterating through all the strings.

The test cases provided in the script pass the function's output to the `longest` function with different input lists and verify the behavior of the function.