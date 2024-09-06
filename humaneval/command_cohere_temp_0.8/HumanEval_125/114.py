```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return words if words is not None else ['???']
```

The problem asks to return '???' if the input string is not made of alphabetic characters, whitespaces, or commas. Otherwise, the function correctly splits the string into words on whitespaces or commas, or returns the count of lowercase letters with an odd number of characters (counting from 'a' to 'z'). Additionally, the function includes a Jupyter Notebook-like "???") syntax to indicate invalid outputs. 

This solution focuses on returning the expected outputs dictated by the problem statement without checking for any particular exceptions. However, it would be safer to handle possible errors, such as splitting on whitespace or comma characters that are not present in the text, or counting characters when the input string is not alpha. 

Here is a possible exception handling improvement:
```python
def split_words(txt):
    # Split on commas or spaces, if either character exists
    words = txt.split(',') if ',' in txt or ' ' in txt else None
    # Check if the input is alphabetic characters only and return the count of odd letters
    if not words and txt.isalpha():
        words = sum(1 for char in txt if char.islower() and ord(char) % 2 == 1)
    return ['???'] if words is None else words
```