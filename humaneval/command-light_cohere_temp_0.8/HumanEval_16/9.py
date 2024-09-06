```python
def count_distinct_characters(string: str):
    return len([c for c in string.  if c.isalpha()])
 strings only contain unique, alphabetic characters, so this should be quite efficient.
# Some sample inputs
xyzXYZ
Jerry
```
This code defines a utility function that counts the distinct characters in a given string. It uses a Python list comprehension and a built-in function `isalpha()` to check if each character is in the alphabet. The function then returns the string length, minus any characters that aren not in the alphabet.