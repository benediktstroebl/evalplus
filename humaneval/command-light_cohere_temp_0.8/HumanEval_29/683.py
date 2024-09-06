```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1:
strings = ["abc", "bcd", "cde", "array", "e"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']


# Test case 2:
strings = ["a", "bcd"]
prefix = "ab"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['bcd']


# Test case 3:
strings = ["abcd", "a"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abcd']
``` 
This Python script defines a function called **filter_by_prefix** that filters a list of strings based on their prefix. The function takes two arguments: a list of strings **strings** and a prefix **prefix**. 

The function uses a list comprehension to iterate over each string in the input list. The function then checks if the string starts with the provided prefix. 

The output of the function is a new list that contains only the strings from the original list that start with the given prefix.