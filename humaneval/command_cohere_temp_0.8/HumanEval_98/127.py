Here's the Python code with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    upper_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```

This script provides a function `count_upper()` that takes a string as input and returns the number of uppercase vowels in even indices of the string. It utilizes a set called `upper_vowels` to efficiently check if the char at each even index is an uppercase vowel or not, and counts them using a `count` variable. The given examples in the docstring yield the correct results with this updated code.