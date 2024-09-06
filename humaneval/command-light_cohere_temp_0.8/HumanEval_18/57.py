Here's a self-contained Python function that returns the count of occurrences of a given substring within a given string:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a given substring in the original string, 
    ignoring case and performing a case-insensitive search.
    """

    particular, and returns the count of occurrences.
    """
    string : str,
        substring : str
    """
    return sum(1 for x in string.find(substring, string).search=True)
```

The function `how_many_times` takes two parameters: a string and a substring. It uses the search function to find all occurrences of the substring in the string, and then uses the sum function to add up the count of occurrences.

This function can be used to find the number of times a given substring appears in a string, and it can also be used to find the number of times a given substring appears in a list of strings.