Here's a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, ignoring case.
    Args: 
    - string: str -- The input string to check for distinct characters
    Returns: 
    int -- The count of distinct characters
    """
    # Remove all lowercase and uppercase characters
    string = string.casefold('', '').

    # Initialize a set to keep track of distinct characters only
    distinct_set = set()

    # Convert the string to a list of characters to make set operations efficient
    characters = string.split()

   
    empty_character = ''

    # Add all distinct characters to the set
    for char in characters:
        distinct_set.add(char)

    # Count the number of distinct characters
    return len(distinct_set)
```
This function:
- Takes a string as an argument
- Returns an integer (count of distinct characters)
- The function first makes the string all lowercase (or uppercase) to ensure that the result is case-insensitive. Then, it creates a set to only store distinct characters from the original string. Finally, it counts the number of distinct characters in the set and returns it as the result.

This function can be used to quickly and efficiently find the number of distinct characters in any given string.