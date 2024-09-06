Here's the improved Python code with comments and proper formatting:
```python
def how_many_times(string, substring):
    """ 
    Find how many times a given substring can be found in the original string.
    > overlapping matches are
    We return the number of non-overlapping occurrences. 
"""
    # Initialize a count of zero
    count = 0

    # Iterate over each character in the string
    for i, char in enumerate(string):
        # Check if the character is the substring
        if char == substring:
            count += 1

    return count
```