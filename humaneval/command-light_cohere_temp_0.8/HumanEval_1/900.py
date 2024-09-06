Here is a self-contained Python script that defines a function called `separate_paren_groups` which solves the problem of separating groups of parentheses:
```python
def separate_paren_groups(s):
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return a list of separated strings.
    """ Separate groups of balanced parentheses.
    """ each open brace is closed and not nested within each other.
    """

    string to split
    """
    """
    def split(string):
        # Create an empty list to store the split strings
        result = []
        
        # Loop through each character in the string
        for char in string:
            if char == ')':
                # If the character is a right parenthesis, add it to the result list
                result.append('(')
                # Reset the string to continue searching for the next parenthesis
                string = string[string.find(')') + ' '
            else:
                # If the character is not a right parenthesis, add it to the result string as is
                result.append(char)
        return result
    
    return split(s)
```
This function takes a string `s` as input and returns a list of separated strings. 

The function uses a simple recursive approach to split the string.