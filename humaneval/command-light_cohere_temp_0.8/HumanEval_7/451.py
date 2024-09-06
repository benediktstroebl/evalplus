The solution is a Python function `filter_by_substring` that filters a list of strings based on whether the string contains a given substring. 

```python
import typing


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]


# Test cases 
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a" 

# expected output: ['abc', "bacd", "array"]
print(filter_by_substring(strings, sub))
```

The code defines a function that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the substring. The test cases show how the strings are passed to the function and the expected output is printed to compare with the actual output.