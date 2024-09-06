```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string as an argument and counts the number of uppercase vowels in even indices of that string. The function then returns the count of uppercase vowels in even indices. 

The program passes the test cases provided in the original task description, which are:
```
>>> count_upper('aBCdEf')
1
>>> count_upper('abcdefg')
0
>>> count_upper('dBBE')
0
```

These tests examine the functionality of the `count_upper()` function concerning its expected behavior as described in the problem statement.