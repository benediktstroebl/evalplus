Here's a Python script that contains a function `count_upper()` which solves the problem as described in the markdown code block:
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

This function takes a string s as input and counts the number of uppercase vowels in even indices. It does so by first creating a boolean variable called vowels, which contains the uppercase vowels 'AEIOU'. It then iterates through the characters in the string s in increments of 2 using the range function with a starting index of 0 and a stopping index that is one less than the length of s. It determines whether the character in each iteration index is an uppercase letter using the isupper() method. If so, it additionally checks whether the character is in the vowels string. If both conditions are met, it increments the count variable by 1. Eventually, the function returns the count.

This solution efficiently solves the problem in a single piece of code and can be directly copied and run.