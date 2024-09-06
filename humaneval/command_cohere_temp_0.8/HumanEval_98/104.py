Here's a Python script that contains a function named `count_upper()` which solves the problem as outlined in the markdown code block you provided:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'[AEIOU]{2,}(?![AEIOU])')
    matches = pattern.findall(s)
    return len(matches)
```

This function uses regular expressions to match strings that have two or more consecutive uppercase vowels, specifically looking for instances where these combinations are in even positions in the string and are not followed by another uppercase vowel. The `findall()` method provides an array of all matches, and `len()` is then used to count the number of matches, which corresponds to the number of uppercase vowels in even indices of the given string.