```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    
    Parameters:
    text (str): The input string.
    
    Returns:
    str: The string without vowels.
    """
    # Define vowels in both lowercase and uppercase
    vowels = 'aeiouAEIOU'
    
    # Use a list comprehension to filter out vowels
    filtered_text = [char for char in text if char not in vowels]
    
    # Join the filtered characters back into a string
    return ''.join(filtered_text)


# Test the function
if __name__ == "__main__":
    print(remove_vowels(''))
    print(remove_vowels("abcdef\nghijklm"))
    print(remove_vowels('abcdef'))
    print(remove_vowels('aaaaa'))
    print(remove_vowels('aaBAA'))
    print(remove_vowels('zbcd'))
```

This Python script defines a function called `remove_vowels` that takes a string as input and returns the string without vowels. It uses a list comprehension to filter out vowels from the input string and then joins the remaining characters back into a string. The test cases at the end of the script demonstrate the function's behavior.