Here's a Python script that contains a function to solve the problem:
```python
def count_upper(s):
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. The function utilizes a loop to iterate through the string, checking every second index for an uppercase vowel. The `isupper()` method checks if a character is uppercase, while `in 'AEIOU'` checks if it's a vowel. The variable `cnt` keeps track of the count, which is returned at the end.

This approach ensures the function is self-contained and capable of solving the given problem without relying on external modules or tools.