Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    def has_vowels(c):
        vowels = 'AEIOUaeiou'
        return c.isupper() and c in vowels

    return sum(1 for i, char in enumerate(s, 2) if has_vowels(char) and i % 2 == 0)
```
This script defines a function `count_upper()` that:
1. Defines a helper function `has_vowels()` to determine if a character is an uppercase vowel.
2. Utilizes a sum() function to iterate through characters in the string `s` at even indices only.
3. Increments the count for each character if it's an uppercase vowel.

This solution adheres to the problem's expectations and demonstrates efficient string manipulation and functional programming. Feel free to modify the tests or ask any questions about the solution! Let me know if you would like to discuss further insights or alternative approaches.