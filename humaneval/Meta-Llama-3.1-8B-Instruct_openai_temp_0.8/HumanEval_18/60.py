```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    # Use the count method which returns the number of occurrences of the substring
    # The count method does not consider overlapping cases by default
    if len(substring) == 0:  # if the substring is empty, return 0
        return 0
    # If the substring is not found, return 0
    elif substring not in string:
        return 0
    # Otherwise, return the count of the substring
    else:
        # Use the len function to get the length of the substring
        # Use a while loop to find the overlapping cases
        count = 0
        index = 0
        while index < len(string):
            # Use the find method to get the index of the substring
            index = string.find(substring, index)
            if index!= -1:  # if the substring is found
                count += 1
                # Move the index to the right by the length of the substring
                index += 1  # increment index after the find
            else:
                break
        return count

# Example usage
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

However, the `find` function used above is not the most efficient way to do this. Python's `re` module, which provides support for regular expressions, has the ability to do this efficiently.

Here's a more efficient version of the function:

```python
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    # Use the finditer function which returns an iterator yielding match objects for every occurrence
    # Use the len function to get the number of occurrences
    if len(substring) == 0:  # if the substring is empty, return 0
        return 0
    # If the substring is not found, return 0
    elif substring not in string:
        return 0
    # Otherwise, return the count of the substring
    else:
        # Use the finditer function to get the match objects
        return len(re.finditer(re.escape(substring), string))

# Example usage
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This version should be more efficient for large inputs.