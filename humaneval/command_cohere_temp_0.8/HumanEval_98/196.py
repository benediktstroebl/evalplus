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

This function accepts a string s and scans it sequentially in intervals of 2. It determines if each character is an uppercase vowel and tallies the count of such characters. The loop skips every odd index, ensuring only even indices are considered. The function ultimately returns the total count of uppercase vowels in even indices of the input string.

To ensure the functionality, here is a testing string for which you can verify the output:
```python
test_string = 'aBCdEf'
print(count_upper(test_string))  # Output: 1
```

This should return `1` as the only uppercase vowel in an even index is the character 'E' in the test string.