```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This Python script defines a function `count_upper` that takes a single argument - a string `s`. The function counts the number of uppercase vowels in even indices of the string and returns the result. 

To do this, it initializes a counter `cnt` to 0 and iterates over the characters of `s` in steps of 2 (i.e., even indices) using a `for` loop with the `range` function and the length of the string. For each character at an even index, it checks if it is an uppercase vowel using the `isupper` method and the member test `s[i] in 'AEIOU'`. If both conditions are met, it increments the count `cnt`. 

The given examples in the comment on the problem are correctly solved by this function:
- `count_upper('aBCdEf')` returns 1, as the uppercase vowel is 'E' at index 2. 
- `count_upper('abcdefg')` returns 0, as there are no uppercase vowels in even indices. 
- `count_upper('dBBE')` returns 0, as there are no uppercase vowels in even indices. 

Overall, this is a well-written Python script that solves the problem correctly and efficiently.