Here's a Python script with a function that solves the problem as described in the code block:
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

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a list `vowels` to store the uppercase vowels and loops through the input string in increments of 2 to check for valid vowels located at even indices. The function returns the count of uppercase vowels in even indices. 

You can use this function to solve the problem as demonstrated through the tests provided earlier.