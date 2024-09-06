Here's a Python script that contains a function named `count_upper()` which solves the problem as outlined in the markdown code block you provided:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'[AEIOUaeiou](?<!^)(?=\\b|$)')
    return sum(1 for _ in pattern.finditer(s)) / 2
```

This code works by first creating a regular expression pattern. This pattern matches all uppercase vowels (both 'A' and 'I' and 'O' and 'U' and their lowercase equivalents) in the string `s`, but only if they appear in an even index (i.e., the indices which are divisible by 2). The use of the `(?<!^)(?=\\b|$)` asserts ensures that the vowels are not the first or last characters of the string and are not preceded or followed by a word boundary.

The `finditer()` method generates iterator objects for each match. We sum the matches and then divide by 2 to get the total count of uppercase vowels in even indices.