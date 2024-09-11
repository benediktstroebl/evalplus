### Remove Vowels from a String
#### Problem Description
The `remove_vowels` function removes all vowels from a given string.

#### Code
```markdown
def remove_vowels(text):
    """
    Remove all vowels from a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string without vowels.
    """
    # Define a string of vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels from the input string
    # The `filter` function is used to create a new string without vowels
    result = ''.join(filter(lambda char: char not in vowels, text))
    
    return result

# Test cases
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```
This script defines the `remove_vowels` function, which takes a string as input and returns the string without vowels. The function uses a list comprehension to filter out vowels from the input string and then joins the result into a new string. The test cases at the end demonstrate the function's behavior.