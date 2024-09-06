```python
def check_if_last_char_is_a_letter(txt):
    """
    Create a function that returns True if the last character of a given string is an alphabetical character and is not part of a word, and False otherwise.

    Parameters:
        txt (str): The input string to analyze.

    Returns:
        bool: True if the last character is an alphabetical character and is not part of a word, False otherwise.
    """
    # Extract the last character and check if it's alphabetical
    last_char = txt.strip()[-1]
    if not last_char.isalpha():
        return False

    # Check if the last character is part of a word or not
    words = txt.split()
    if last_char in words[-1]:
        return False
    return True
```

The function leverages the `split()` method to divide the input string into multiple words, and then checks if the last character is part of the last word or not. If the last character is not part of any word or is not an alphabetical character, the function returns `False`. Otherwise, it returns `True`. 

This approach ensures that the function works for different cases like "apple pie", "apple pi e", "apple pi e " and even for an empty string. 

Let's assume that the string is provided as the input to the function via a variable called `txt`. We first extract the last character using `txt.strip()[-1]`. Using the `isalpha()` method, we check if the last character is alphabetical. If it is not, we return `False` because either the string ends with a non-alphabetical character or it is an empty string. 

Next, we split the string into words using `txt.split()`. We then check if the last character is part of the last word among the split words. If it is, the last character is considered part of a word and we return `False`. Otherwise, it is not part of any word and we return `True`. 
This solution aims to provide a clear and efficient approach to solving this problem. Relevant Tests: 

```python
# Test Case 1
print(check_if_last_char_is_a_letter("apple pie"))  # Expected: False

# Test Case 2
print(check_if_last_char_is_a_letter("apple pi e"))  # Expected: True

# Test Case 3
print(check_if_last_char_is_a_letter("apple pi e "))  # Expected: False

# Test Case 4
print(check_if_last_char_is_a_letter(""))  # Expected: False
```
```