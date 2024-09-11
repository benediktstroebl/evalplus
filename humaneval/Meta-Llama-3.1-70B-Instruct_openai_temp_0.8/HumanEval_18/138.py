```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found.

    """
    # Handle the edge case where the substring is empty
    if not substring:
        return 0

    # Initialize a counter to store the number of occurrences
    count = 0

    # Iterate over the string, considering all possible starting indices
    for i in range(len(string)):
        # Check if the substring matches the string at the current position
        if string[i:i+len(substring)] == substring:
            # If it matches, increment the counter
            count += 1

    # Return the total count of occurrences
    return count

# Example usage:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```
This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, including overlapping cases. It uses a simple iterative approach to scan the string and count the occurrences of the substring.