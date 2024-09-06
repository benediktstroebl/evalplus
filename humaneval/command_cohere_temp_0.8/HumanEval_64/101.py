```python
def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel only at the end of the word."""
    # Your code here!
    vowels = set('aeiou')
    if s.endswith('y'):
        return sum(1 for char in s if char in vowels) + 1
    else:
        return sum(1 for char in s if char in vowels)
```

This code defines a function vowels_count that takes a string s as input and counts the number of vowels in the string, counting 'y' as a vowel only if it is at the end of the word. The function then returns the count of vowels using the `sum` function and a generator expression that iterates over each character in the string `s` and checks if each character is a vowel, using a set `vowels = set('aeiou')` to store the vowels. 

To count 'y' as a vowel only at the end of the word, the code checks if the string ends with 'y' using the `endswith` method, adding 1 to the total count if it does. Otherwise, it returns the count of the other vowels in the string. 

This solution provides a clear and efficient approach to solving the problem and meets the criteria of being a self-contained code block.  If there is anything else I can help you with, let me know!