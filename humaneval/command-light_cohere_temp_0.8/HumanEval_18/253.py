```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function counts the occurrences of a given substring within the original string, while handling overlapping substring matches.
    :string - split into individual characters
    str.join and then strings are compared to split into individual characters
    - Iterate through each character and count how many times the substring appears while skipping duplicates
    - Return the count of occurrences
    """
    string = str(string)  # Convert string to a list of characters
    sub = str(substring)  # Convert substring to a list of characters
    count = 0  # Initialize count

    # Iterate through each character in the string
    for char in string:
        if char in sub:  # Check if the character is in the substring
            count += 1

    return count  # Return the count of occurrences
```