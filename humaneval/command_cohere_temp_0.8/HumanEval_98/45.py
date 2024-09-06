Here's the Python code to solve the problem:
```python
def count_upper(s):
    c = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            c += 1
    return c
```

The code defines a function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices using a loop that iterates through the string at every second index. It checks if the character is an uppercase vowel using the `isupper()` method and checks if it is one of the uppercase vowels 'AEIOU' using membership testing. The count is returned as a result.