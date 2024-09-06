```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function with sample inputs and expected outputs
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Test case 1
result1 = filter_by_substring(strings, substring)
print("Test case 1: " + result1)

# Test case 2
result2 = filter_by_substring([strings[0]], substring)
print("Test case 2: " + result2)

# Test case 3
result3 = filter_by_substring(strings, substring)
print("Test case 3: " + result3)

# Test case 4
result4 = filter_by_substring([strings[1], strings[2]], substring)
print("Test case 4: " + result4)

# Test case 5
result5 = filter_by_substring(strings[:2], substring)
print("Test case 5: " + result5)
```
The function `filter_by_substring` filters an input list of strings for ones that contain a given substring. It uses list comprehension to iterate over the input strings and returns a new list containing only the strings that contain the specified substring.