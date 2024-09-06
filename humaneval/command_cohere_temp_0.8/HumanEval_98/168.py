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

This function accepts a string s and scans it sequentially in increments of 2. It determines if each character is an uppercase vowel and tallies them. The loop's increment of 2 ensures investigation of even indices only. The function returns the total count of uppercase vowels in even positions.

The expected behavior for the provided test cases is:
```python
print(count_upper('aBCdEf')) -> 1
print(count_upper('abcdefg')) -> 0
print(count_upper('dBBE')) -> 0
```