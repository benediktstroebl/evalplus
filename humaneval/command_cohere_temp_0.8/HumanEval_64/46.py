```python
def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel only at the end of the word."""
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels or (char == 'y' and s[-1] == char):
            count += 1
    return count
```

To count the number of vowels in a string, we iterate through each character in the given string and check if it is a vowel or 'y' (which is considered a vowel only at the end of the word). We increment the count variable for each valid vowel encountered. This approach ensures the functionality described in the problem statement.