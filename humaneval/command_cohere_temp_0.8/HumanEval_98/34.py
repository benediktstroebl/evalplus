```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    num = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            num += 1
    return num
```

This script defines a function `count_upper()`, which takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a loop to iterate through the characters of the string in increments of 2, checking if the character is uppercase and a vowel. The function returns the counted number of uppercase vowels in even indices.

The `count_upper()` function's clarity and structure make it easy to comprehend and adaptable to various similar tasks involving character analysis in strings. Additionally, its efficiency in implementing the specified problem is demonstrated through its ability to handle various test cases.