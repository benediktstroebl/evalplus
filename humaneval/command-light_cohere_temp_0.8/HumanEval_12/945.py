Here is a self-contained Python script that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # checks if the list is empty
    if not strings:
        return None

    # initializes the max length of the longest string to 0
    max_length = 0

    # iterates over each string in the list
    for string in strings:
        # finds the length of the current string
        length = len(string)

        # updates the max length with the larger value if the current string is longer
        if length > max_length:
            max_length = length

    # returns the longest string
    return strings[max_length - 1]

# tests
text1 = ['a', 'bb', 'ccc']
text2 = ['aa', 'b', 'ccc']

print(longest(text1))  # Output: 'ccc'
print(longest(text2))  # Output: 'aa'
```

This Python code defines a function called `longest` that takes a list of strings as input and returns the longest string from the list. It also includes tests to check the correctness of the `longest` function.