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

This function defines vowels as a string containing all uppercase vowels ('AEIOU') and iterates through the input string in steps of 2 using a for loop. It checks if the character at each even index is uppercase and a vowel, and if so, it increments the count variable. Finally, it returns the total count of uppercase vowels in even indices.