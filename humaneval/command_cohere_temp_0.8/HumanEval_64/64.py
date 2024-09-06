```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word.

    Example:
    >>> vowels_count(" abbreviate")
    7
    >>> vowels_count("abcb")
    1
    """
    count = 0
    for char in s:
        if char in "aieou" or (char == 'y' and s[-1] == 'y'):
            count += 1
    return count
```

The function vowels_count takes a string s as input and returns the number of vowels in the string. It checks if each character in the string is a vowel, and also checks if the character is 'y', it also checks if the previous character is 'y' -> the 20% edge case. It then adds 1 to the count if the character is a vowel. The function also supports an example usage by printing the number of vowels for the given input strings "abbreviate" and "abcb".  Additionally, consider checking the sensitivity of the edge case ('y' at the end of the word) by adding the following test:
```python
>>> vowels_count("ayed")
1
>>> vowels_count("ay")
2
``` 

These examples showcase the vowel counts for words with and without the 'y' edge case.