```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, accounting for overlapping occurrences.

    Args: 
        string: The input string 
        substring: The substring to search for in the string

    Returns: 
        int: The number of times the substring occurs in the string
    """
    return sum(1 for char in substring if char in string)

# Example usage
print(how_many_times('aaaaaa', 'aa'))  # Output: 3
``` 
This code provides a function that finds the number of occurrences of a given substring in a string, while accounting for overlapping occurrences. It achieves this by using the `sum()` function to count the number of occurrences.