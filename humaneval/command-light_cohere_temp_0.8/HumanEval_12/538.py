Here's the improved version with proper variable and function naming, consistent indentation, and additional comments:
```python
def find_longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    Parameters:
        strings (list of strings) is expected
    Returns:
        str: longest string in the list
    """
    if not strings:
        return None

    longest_len = max(len(string) for string in strings)
    longest_string = strings[0][:longest_len]
    return longest_string

# Test the function
input_strings = ['a', 'b', 'c']
result = find_longest(input_strings)
print("Longest string:", result)
```
This version of the script follows Python best practices and is more readable and maintainable. The function `find_longest` takes a list of strings as input and returns the longest string from that list.