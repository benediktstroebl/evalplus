```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    def count_vowels(string):
        vowels = {'A', 'E', 'I', 'O', 'U'}
        return sum(1 for char in string if char in vowels)
    
    return sum(count_vowels(s[i]) for i in range(0, len(s), 2))
```

The nested function `count_vowels` is introduced to avoid repeated code and checks for characters in a predefined set of vowels. The outer function then leverages this helper function to determine if the vowel is in an even index position.