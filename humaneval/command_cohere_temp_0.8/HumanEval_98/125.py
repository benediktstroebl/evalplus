```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i].lower() in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string `s` as input and first iterates through it, visiting every second index using the `for i in range(0, len(s), 2)` loop. Within the loop, it checks if the character at that index is an uppercase vowel using a combination of `s[i].isupper()` and `s[i].lower() in 'AEIOU'`. The `isupper()` method checks if the character is uppercase, and `in 'AEIOU'` checks if it's a vowel. The total count is then returned as the result.

This solution efficiently computes the answer without introducing any extra complexity, making it an optimized solution to the problem. 

**NOTE:** The loop iterates every second index, due to the range clause `range(0, len(s), 2)`. This is half the indices of the string, which is precisely the odd indices in the string. This is intuitive since the even indices are where the function intends to count the uppercase vowels.