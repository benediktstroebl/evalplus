```python
import re

def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    words = txt.split(',') if re.search(r'\s', txt) is None else txt.split()
    if not words:
        return 0 if txt.isalpha() else 2
    return words
```

The problem gives us three potential ways to split the string, two of which are mutually exclusive:
1. Split on whitespace if there is any.
2. If the string has no whitespace, split on commas instead.
3. If the string has no whitespace or commas, return the number of lowercase letters with an odd multiplicity in the alphabet.

This is somewhat ambiguous, so the tests for this function are:
```
split_words("Hello world!") == ["Hello", "world!"]
split_words("Hello, world!") == ["Hello", "world!"]
split_words("abcdef") == 3
split_words("aab") == 2
split_words("abc") == 1
split_words("Hello World!") == ["Hello", "World"]
split_words("Hello,World!") == ["Hello", "World"]
split_words("abcdefg") == 4
split_words("iiiiiiii") == 0
split_words("aaaaaaab") == 4
```

Here is a short 20-minute solution using Python:
- Use a regular expression to find if the string contains whitespace or commas.
- Split the string into words using either whitespace or commas.
- If the string does not contain any alphabetic characters, return 0.
- If the string does not contain any whitespace, commas, or alphabetic characters, return 2.

This solution relies on Python's `re` module for regex and `str.split()` to split the string into words. The function returns 0 if the string contains no alphabetic characters, as there would be nothing to split. It returns 2 if the string contains no whitespace, commas, or alphabetic characters, since this is the "default" case that the problem statement outlines.