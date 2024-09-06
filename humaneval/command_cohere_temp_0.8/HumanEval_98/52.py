```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string `s` as its argument and first initializes a counter `cnt` to 0. It then iterates through the string, checking if the index of each character is even and if the character is an uppercase vowel. If both conditions are met, the counter is incremented by 1. Finally, the function returns the value of the counter, thus providing the number of uppercase vowels in even indices of the given string. 

This approach ensures that the problem is correctly solved without introducing any extra dependencies that could lead to errors or introduce bugs.