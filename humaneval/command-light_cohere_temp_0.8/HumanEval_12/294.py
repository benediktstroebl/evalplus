```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list of strings.
    """
    strings = [str.join for sub in strings if sub!
    return max(sub, key=len(sub))

# Test the function
test_longest = [
    "Hello World",
    "Python is Great",
    "This is a Long String",
    "Python"
]
print( longest(test_longest) )

test_longest2 = [
    "Python",
    "Pyth",
    "Python"
]
print(longest(test_longest2)) )
```

The provided code defines a function `longest` that takes a list of strings as input and returns the longest string from that list. The function uses the max function with the key parameter set to the length of each string to find the maximum length and return the corresponding string. This code also includes two test cases that demonstrate the functionality of the function.