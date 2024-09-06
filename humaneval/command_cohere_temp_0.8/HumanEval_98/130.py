Here's the Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function defines a set of uppercase vowels and then uses a loop to iterate through the string s, checking for uppercase vowels in every second index (i.e., in the even indices). It then counts the number of matches and returns the count.

If the input is the string 'aBCdEf', the function will return 1, and it will return 0 for the strings 'abcdefg' and 'dBBE', respectively.