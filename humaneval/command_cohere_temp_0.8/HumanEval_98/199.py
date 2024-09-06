Here's a Python script that contains a function named `count_upper()` which solves the problem as outlined in the markdown code block you provided:
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

This function takes a string s as input and counts the number of uppercase vowels in even indices. It does so by first creating a boolean variable called vowels, which contains the uppercase vowels ('AEIOU'). Then, it increments a counter variable count each time it finds an uppercase vowel in an even index. The function iterates through the string s, checking for uppercase vowels in each index, and skips every other index (i.e., even indices) as specified by the problem. Finally, the function returns the count of uppercase vowels in even indices.