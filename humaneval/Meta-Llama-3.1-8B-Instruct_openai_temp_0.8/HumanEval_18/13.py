```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the original string.
    """

    # If the substring is empty or the string is empty, return 0
    if not substring or not string:
        return 0

    # Initialize a counter to track the number of occurrences
    count = 0

    # Calculate the length of the substring
    substring_length = len(substring)

    # Iterate over the string, considering each character as a potential start of the substring
    for i in range(len(string)):
        # Check if the substring matches the string starting from the current position
        if string[i:i + substring_length] == substring:
            # If it matches, increment the counter
            count += 1

    # Return the total count
    return count

# Example usage
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This code defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring appears in the string. It uses a simple iteration approach to count the occurrences, considering overlapping cases. The example usage demonstrates the function's correctness with the provided unit tests.