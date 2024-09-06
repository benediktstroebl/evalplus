Here's a self-contained Python function that solves the given string-finding problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    considering overlapping matches.
    Example the how string as a substring 
    e.g. 'aaaa... Suiteds' string
    string: 'aaaaaaa' 
    substring: 'aa' 
    Returns:  3 
    """
    return len(string.find(substring, string))
``` 
This code defines a function that takes two parameters: string and substring, and returns an integer representing the number of occurrences of the substring in the string. It uses the string.hash() function to find the string and substring and calls the find() method, passing in the substring and the original string as arguments. The find() method returns a index of the first occurrence of the substring in the string.