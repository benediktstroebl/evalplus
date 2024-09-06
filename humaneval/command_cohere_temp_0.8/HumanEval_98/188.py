```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    uppercase_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string `s` as input and returns the number of uppercase vowels in even indices of that string. The function first creates a set of all uppercase vowels, then iterates through the string `s` by stepping two characters at a time (using a range of sizes equal to half the length of the input with step 2). It checks each character in these even positions to see if it's a member of the uppercase vowel set, and if it is, it increments a count variable. The function finally returns the final count.

This approach ensures the function is concise and efficient in solving the problem statement and passes the given tests.