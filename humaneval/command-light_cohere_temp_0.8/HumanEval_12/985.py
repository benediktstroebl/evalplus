```python
def longest(strings: List[str]) -> Optional[str]:
    # Set a default return if the list is empty
    if not strings:
        return None
    
    # Initialize the variable to store the length of the longest string
    max_length = 0
    longest_string = ""

    # Iterate through the list of strings and find the longest
    for string in strings:
        # Calculate the length of the current string
        length = len(string)
        # Update the longest_string with the current string and its length
        longest_string = string
        max_length = max(length, max_length)

    # Return the longest string found
    return longest_string

# Example usage
# Test the function
test_longest = [ longest(["a", "bb", "ccc"]) ]
 assert test_longest == "ccc"

# Test with an empty list
test_empty = [ longest([]) ] ]
 assert test_empty is None
```