Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Use a dictionary to store the number of uppercase vowels in each index.
    d = {i: 0 for i in range(len(s))}
    # Count the number of uppercase vowels.
    for i in range(len(s)):
        if s[i].isupper() and s[i] in 'AEIOU':
            d[i] = d[i+1] + 1
    # Count the number of uppercase vowels in even indices.
    return sum(d[i] for i in range(len(s)) if i % 2 == 0)
```

This script provides a function `count_upper()` that takes a string as input and returns the number of uppercase vowels in even indices. It utilizes a dictionary to keep track of the number of uppercase vowels in each index and iterates through the string to populate the dictionary. Finally, it checks for even indices and computes the count before returning the result.