Here's the Python code with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a loop that iterates through the string at twice the speed (using `range(0, len(s), 2)`), checking for uppercase vowels in each even index.