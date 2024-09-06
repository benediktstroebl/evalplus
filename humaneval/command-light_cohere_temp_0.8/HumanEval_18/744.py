Here is a self-contained Python function that solves the problem of counting the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times a given substring can be found in the original string.

    Args:
        string (str) = The input string
        substring (sub) = The substring to find

    Returns: number_of_occurrences (int)
    """
    # Split the string
    words = string.split()
   
    words = [word for word in words if word == substring]
    # Count the occurrences
    return len(words)
```

This function takes two parameters: `string` (the input string) and `substring` (the substring to find). It uses the `split split()` method to split the input string into individual words, and then it creates a list of words containing only the occurrences of the `substring`. The function then returns the count of these words, which corresponds to the number of times the `substring` can be found in the original string.