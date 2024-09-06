Here's the Python code to solve the problem:
```python
def count_upper(s):
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This code defines a function `count_upper()` that takes a string `s` as input and calculates the number of uppercase vowels in even indices using a set of uppercase vowels and a loop that checks through the string at even indices. It then returns the count.