### Flip Case Function in Python

Here's a self-contained Python script that includes a function to flip the case of a given string:

```markdown
### Code
```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

### Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # Output: 'hELLO'
    print(flip_case('hELLO'))  # Output: 'Hello'
```

### Explanation
This script defines a function called `flip_case` that takes a string as input. It uses a generator expression to iterate over each character in the string. For lowercase characters, it converts them to uppercase using the `upper()` method, and for uppercase characters, it converts them to lowercase using the `lower()` method. The `join()` method is then used to combine the modified characters back into a string. The function returns this new string. 

Finally, the script includes a test to demonstrate the function's behavior.