Here's the Python script with a function that solves the problem:
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

This script defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices. The function first creates a variable `vowels` that stores the uppercase vowels: 'AEIOU'. It then initializes a counter variable `count` to 0. The function then loops through the characters of the input string `s` in steps of 2 (i.e., even indices) and checks if the character is uppercase and a vowel. If it is, the counter is incremented. Finally, the function returns the value of the count.

This solution corresponds to the problem statement and passes the tests provided. 
For example, in the first test of the problem:
```python
assert count_upper('aBCdEf') == 1
```

The script returns 1, which is the correct answer, since the uppercase vowel 'E' is at position 2 (an even index). 

In the second test:
```python
assert count_upper('abcdefg') == 0
```

The script returns 0, as there are no uppercase vowels in even indices in the string. 

Finally, for the third test:
```python
assert count_upper('dBBE') == 0
```

The script again returns 0, as there are no uppercase vowels in even indices in the string.