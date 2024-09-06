```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] in 'AEIOU':
            cnt += 1
    return cnt
```

The `count_upper` function iterates through the characters of the input string `s`. When the character index is even, and the character is an uppercase vowel ('AEIOU'), it increments the `cnt` variable by 1. The function returns the final count of uppercase vowels in even indices. 

This approach ensures that the problem is correctly solved, as demonstrated by the test cases, but without unnecessary character checks that were not specified in the original prompt.