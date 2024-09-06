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

This function takes a string s as input and counts the number of uppercase vowels in even indices. It does so by first creating a vowels string that holds all uppercase vowels and then iterating through the input string s in steps of 2 (i.e., even indices) and counting the number of occurrences of uppercase vowels in these indices, using the isupper() string method and an explicit check for the vowels characters. The function returns the final count of uppercase vowels in even indices.