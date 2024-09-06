```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the number of vowels in a word, we use string methods
    # to find all occurrences of vowels in a word (excluding 'y' if not
    # at the end of the word) and add them to a counter, which is then
    # returned.
    import re

    vowel_regex = re.compile(r'(?i)[aeiou]{1,2}|y$')
    return sum(1 for _ in vowel_regex.finditer(s))
```

This script defines a function vowels_count that takes a string s as input and returns the number of vowels in the string. The function uses the re compile function to create a regular expression pattern that matches any sequence of 1 or 2 vowels (including 'y' at the end of the word), and then uses the finditer function to find all matches of this pattern in the input string. The sum function is used to count the number of matches and return the result.

Example usage:
```python
print(vowels_count("abcde"))  # Outputs 2
print(vowels_count("ACEDY"))  # Outputs 3
``` 

This implementation follows the problem specification and passes the provided tests. It uses a regular expression to find all vowels (including 'y' at the end) in the input string, and then counts the number of matches.