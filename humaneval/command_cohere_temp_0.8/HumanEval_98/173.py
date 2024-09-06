Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function defines a list of uppercase vowels to be used later for the checking process. It then loops through the passed string **s** in increments of 2 to check for uppercase vowels in even indices. It uses the isupper() function to check if the character is uppercase and uses the membership operator `s in vowels` to check if the character is a vowel, and if both conditions are met, it increments the count variable by 1. Finally, it returns the variable count, which holds the number of uppercase vowels in even indices.