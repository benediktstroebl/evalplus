Here's a Python script that contains a function named `count_upper()` which solves the problem as per the provided markdown code block:
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

This function accepts a string s and scans it sequentially in intervals of 2. It determines if each character at even indices is an uppercase vowel, and accordingly increments a count variable. The function returns the final count of uppercase vowels in even indices.

To test this function, you can use the following code:
```python
test_str = 'aBCdEf'
test_str2 = 'abcdefg'
test_str3 = 'dBBE'

print(count_upper(test_str))  # 1
print(count_upper(test_str2))  # 0
print(count_upper(test_str3))  # 0
```

This will output:
```bash
1
0
0
```

The function passes these straightforward tests. You can further enhance the function or broaden the spectrum of tests to check for edge cases and enhance its overall reliability.