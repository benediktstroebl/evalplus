Here's a Python script with a function that solves the problem as described in the code block:
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

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a loop that iterates through the string at 2-character intervals, checking if each character is an uppercase vowel. The total count of such characters in even indices is then returned.

To test this function, you can use the following examples:
```python
print(count_upper('aBCdEf')) # Output: 1
print(count_upper('abcdefg')) # Output: 0
print(count_upper('dBBE')) # Output: 0
```

Each of these examples should yield the expected output as described in the problem statement.