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

This function defines vowels as a string containing the uppercase vowels 'AEIOU' and then uses a loop to iterate through the characters of the input string s. It checks if the character is uppercase and belongs to the set of vowels. If it does, and it appears in an even index (checked by the modulo 2 operation), it increments the count variable. Finally, it returns the total count of uppercase vowels in even indices.