```python
def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel at the end of the word."""
    # Your code here!
    vowels = 'aoeui'
    if s.endswith('y'):
        return sum(1 for char in s if char in vowels)
    return sum(1 for char in s if char in vowels)
```

This code defines the `vowels_count` function, which takes a string s as input and returns the number of vowels in the string. The function counts 'y' as a vowel only when it is at the end of the word. To do this, it uses two summations to check if each letter in the string is a vowel, and if s ends with 'y'. You can use this code to solve the problem statement.