```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a loop to iterate through the string, checking every second index for an uppercase vowel. If an uppercase vowel is found in an even index, the count is incremented. The function returns the final count of uppercase vowels in even indices. 

The examples provided in the prompt will return 1 for `count_upper('aBCdEf')`, return 0 for `count_upper('abcdefg')`, and return 0 for `count_upper('dBBE')`.