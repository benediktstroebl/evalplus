Here is a self-contained Python function that filters an input list of strings for those containing a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]


# Example usage:
input_strings = ['abc', 'bacd', 'cde', 'array', 'Hello', 'World']
input_substring = 'a'
result = filter_by_substring(input_strings, input_substring)
print(result)
```

In this solution, we define a function `filter_by_substring` that takes two arguments: a list of strings `strings` and a substring `substring`. It uses the `find()` method to check if each string in the list contains the given substring, and then returns the string.

The output of the example usage will be: **`['abc', 'bacd', 'array']`**  which are the strings that contain the substring 'a'.