```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU' and i % 2 == 0:
            cnt += 1
    return cnt
```

This function `count_upper` takes a string `s` as its argument and first iterates through its characters. It checks if the character is an uppercase vowel (`s[i].isupper() && s[i] in 'AEIOU'`) and whether its index is even (i % 2 == 0). If both conditions are met, it increments the counter `cnt`. Finally, the function returns the value of this counter.

The given examples in the problem statement would return the following outputs when used with this function:
```python
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))     # Output: 0
```

This script passes the basic test cases for the given problem and thus solves the problem in a self-contained manner, as requested.