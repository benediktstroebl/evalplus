Here's the self-contained Python function that filters an input list of strings for those containing a given substring: 

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
``` 

This function utilizes the `contains` method from the string module to check if each element in the input list contains the given substring.  The function returns a list comprehension to filter out only the strings that contain the substring. 

This is a self-contained solution that does not require any additional functions or modules.