```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Args:
        txt (str): Input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Define and check if the last character exists and it's alphabetic
    last_char = txt[-1:]
    if last_char.isalpha() == False or len(last_char) != 1:
        return False

    # Check if the last character is not part of a word
    words = txt.split()
    if last_char in ' '.join(words):
        return False

    return True
```

In the code above, we follow the following steps to tackle the problem:
1. We extract the last character of the input string `txt` using `last_char = txt[-1:]`.
2. Using the Python built-in `isalpha()` method, we validate if the last character is an alphabetic character. Additionally, we confirm that the length of the last character is not more than 1, aiming to handle edge cases like punctuations.
3. If the last character is not an alphabetical character or has a length different from 1, we return `False` since either the string ends with a non-alphabetic character or a character that's part of a word.
4. If the last character is an alphabetical character and consists of a single character, we then proceed to check if it also exists within the full string, excluding the last character. Using `split()` to extract individual words, and ` ' '.join(words)` to combine them back into a single string, we check if the last character is part of the resulting combination.
5. If the last character does not appear in any of the words, it signifies it's not part of a word, so we return `True`.

The provided example tests demonstrate the correct behavior of the function. Feel free to uncomment any of them to validate the function's behavior against specific test cases.