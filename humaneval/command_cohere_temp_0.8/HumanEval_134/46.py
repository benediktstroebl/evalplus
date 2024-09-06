```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character not part of a word, False otherwise.
    """
    # Extract the last character and remove spaces
    last_char = txt.strip().split(' ')[-1][-1]

    # Check if the last character is in alphabetical order and not part of a word
    return (last_char.isalpha() and not bool(re.search(r'\b\w+\b', last_char)))
```

The function uses several Python features such as regular expressions, tuple unpacking, and the `isalpha()` method to determine whether the last character of the string is in alphabetical order and is not part of a `word`.

Let's break down the solution into steps for clarity:
1. The function takes a string as input and strips any leading and trailing white spaces using the `strip()` method.
2. It then uses tuple unpacking to take the last character of the string `last_char = txt.strip().split(' ')[-1][-1]`. The `-1` indices are used to retrieve the last characters from both the string after white space removal `(txt.strip())` and the split list of words `(txt.strip().split(' '))`.
3. The function then checks if the last character is in alphabetical order using the `isalpha()` method.
4. To check if the last character is part of a word, the function utilizes regular expressions with the pattern `\b\w+\b`, which corresponds to word boundaries (`\b`) and word characters (`\w+`). The `re.search()` function returns a match object if the pattern is found, and `bool(re.search(...))` converts it to a boolean value, where `True` indicates a match, and `False` indicates no match.
5. Finally, the function returns `True` if the last character is an alphabetical character and is not part of a word, and `False` otherwise.

The function highlights Python's built-in methods and powerful regex patterns to solve the problem efficiently and elegantly. 

This approach ensures that the function performs well and is resilient to different scenarios.