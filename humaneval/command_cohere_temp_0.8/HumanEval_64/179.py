```python
def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel at the end of the word."""
    # Your code here!
    vowels = set('aeiou')
    if s.endswith('y'):
        return sum(1 for char in s if char in vowels)
    else:
        return sum(1 for char in s if char in vowels) - (s.count('y'))
```

This script defines a function vowels_count that takes a string s as input and returns the number of vowels in the string, counting 'y' as a vowel only at the end of the word. The code uses a set comprehension to check if each character in the string is a vowel, and counts 'y' as a vowel only at the end of the word. This approach ensures that the function has a time complexity of O(n), where n is the length of the input string s.