```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vowel characters are 'a', 'e', 'i', 'o', 'u', and when the
    last character of the word is 'y' (FIX).
    """
    # define the string of vowels with the y at the end
    vowels = 'aeiouy'
    
    # use the sum function to count the number of vowels in the string
    return sum(1 for char in s if char in vowels)

# here are some test cases
>>> vowels_count("abcde")
2

>>> vowels_count("tetrachromacy")
7

>>> vowels_count("ACEDY")
3

>>> vowels_count("consonant")
1

>>> vowels_count("cyanophage")
4
```