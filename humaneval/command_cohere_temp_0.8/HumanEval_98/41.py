Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU' and s[i].isupper() and (i%2==0):
            cnt += 1
    return cnt
```

This function `count_upper()` takes a string s as input and counts the number of uppercase vowels in even indices. It uses a for loop to iterate through the string, checks if the character is an uppercase vowel and whether its index is even, and increments the counter if both conditions are met. The variable `cnt` keeps track of the count.