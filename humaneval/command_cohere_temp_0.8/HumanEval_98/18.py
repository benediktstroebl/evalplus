Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the markdown code block:
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

This function accepts a string s as input and calculates the number of uppercase vowels it contains that are located in even positions within the string. It achieves this by first creating a vowels string that holds all the uppercase vowels. It then initializes a count variable to 0, which will store the outcome. The function subsequently undergoes the string s in increments of 2, checking each character if it's uppercase and part of the vowels string. Whenever an uppercase vowel is found in an even position, the count goes up. Eventually, the function returns the final count, indicating the quantity of uppercase vowels situated in even indices within the input string.

This code snippet can be tested on its own, and it is designed to be fully independent, meaning it doesn't rely on any external variables or functions other than those explicitly defined within the code block.