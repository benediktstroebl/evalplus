```python
def count_upper(s):
    cnt = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU' and (i%2==0):
            cnt += 1
    return cnt
```

The Python script defines a function `count_upper` taking a string as input and counting the number of uppercase vowels in even indices. It uses a loop to iterate through the characters of the string, checks if the character is uppercase and a vowel, and if it is at an even index, it increments the count. The function returns the final count of uppercase vowels in even indices.