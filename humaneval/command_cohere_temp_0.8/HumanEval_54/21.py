```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```

The function `same_chars()` takes two strings as input and returns a boolean indicating whether the strings have the same characters, with a threshold of 60%. The function compares the sets of characters in both strings, calculates the intersection of these character sets, and divides it by the shorter length of the two strings to determine a percentage cutoff for considering the strings as having substantially the same characters. 

To test this algorithm, you can call the function with different input scenarios and compare the output with the expected truthy or falsey values.