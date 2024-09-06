```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to consider: uppercase AEIOU
    vowels = set('AEIOU')
    count = 0
    for i, char in enumerate(s, start=1):
        if char.isupper() and char in vowels and i % 2 == 0:
            count += 1
    return count
```

This script defines a Python function `count_upper()` that takes a string `s` as input and counts the number of uppercase vowels in even indices of the string. It defines a set of uppercase vowels (`vowels = set('AEIOU')`), and then iterates through the input string, checking if each character is an uppercase vowel and if it's in an even index (using the `enumerate()` function). If both conditions are met, it increments the count. The function returns the final count of uppercase vowels in even indices.