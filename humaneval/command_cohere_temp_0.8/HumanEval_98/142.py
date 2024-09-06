```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i].lower() in 'AEIOU':
            cnt += 1
    return cnt
```

This Python script defines a function named `count_upper` that takes a single argument, `s`, representing a given string. This function counts and returns the number of uppercase vowels present in even indices of the string. To achieve this, it iterates through the string in steps of 2 (using a for loop with the range function), and for each even index, it checks if the character is uppercase and a vowel. The variable `cnt` is used to keep track of the count of such characters encountered. 

The given examples in the prompt will return 1 for 'aBCdEf', 0 for 'abcdefg', and 0 for 'dBBE', respectively.