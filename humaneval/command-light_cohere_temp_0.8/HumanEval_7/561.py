The function `filter_by_substring` takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. It uses the precise and most efficient way to filter the list, which only passes valid strings that contain the given substring. 

The function has the following format:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

In this code, the `contains` method is used to iterate over the list items, and the `contains` method checks if each element contains the substring. 

You can use this function to filter any list of strings for a given substring.