Here's the self-contained Python function that filters an input list of strings for those containing a given substring: 

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello world"]
substring = "a" 

result = filter_by_substring(strings, substring)
print("Filtered list:", result)  # Output: ['abc', 'bacd', 'array']
``` 

This script provides a function that filters and returns a list of strings from an input list, where each string contains the given substring.