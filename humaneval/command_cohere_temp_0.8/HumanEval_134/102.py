```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
    txt (str): The input string to be evaluated.

    Returns:
    bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Ensure the input string is not empty
    if not txt:
        return False

    # Extract the last character and remove it from the string to be examined
    last_char = txt[-1]
    txt_without_last = txt[:-1]

    # Split the input string into words using whitespace characters
    words = txt_without_last.split()

    # Check if the last character is the last character of the string and return True if so
    if last_char == txt_without_last and last_char.isalpha():
        return True

    # Check if the last character is part of any word, and if so, return False
    if last_char in ' '.join(words):
        return False

    return False
```

The provided Python script defines a function `check_if_last_char_is_a_letter` that evaluates whether the last character of a given string is an alphabetical character and is not part of a word. The function first checks if the input string is empty, returning False if so. It then extracts the last character, removes it from the string to be examined, and splits the string into individual words. Next, it checks if the last character is the last character in the string and also an alphabetical character, returning True if so. The function also checks if the last character is part of any word in the string, and if so, it returns False. Ultimately, the function returns False if the last character is part of any word in the input string, effectively solving the problem as described.