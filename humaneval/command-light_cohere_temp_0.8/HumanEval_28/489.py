```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string"""
    
    # Initialize a new string to store concatenation
    result = ""
    
    # Loop through list of strings
    for string in strings:
        # Append current string to the result
        result += string
            
    return result

# Test case 1: empty list
print(concatenate([]))  # Output: ''

# Test case 2: list with one string
print(concatenate(['a']))  # Output: 'a'

# Test case 3: list with more than one string
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This script provides a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test cases are passed to the function to ensure it is working correctly. The output of each test cases will be the concatenated string.