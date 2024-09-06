Here is a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```
This function takes two parameters: `strings`, which is a list of strings, and `substring`, which is a substring to filter within each string.  It provides a filter using a list comprehension to iterate through each string in the list, and checks if each string contains the given substring using the `in` method. 

This function can be easily used in markdown code blocks to filter lists of strings based on a given substring, providing a concise and efficient solution.