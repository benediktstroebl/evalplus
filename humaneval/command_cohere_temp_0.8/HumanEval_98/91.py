```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This script defines a Python function named `count_upper` that takes a string `s` as input and calculates the number of uppercase vowels present in the even indices of the string. It returns the count of uppercase vowels in even positions. The function is designed to comply with the problem statement provided in the original prompt.