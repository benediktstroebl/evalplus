```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This approach involves defining a list `upper_vowels` that stores all uppercase vowels. The function iterates through the string `s` by stepping two indices at a time (odd indices are ignored due to the specification of even indices). It checks if the character at the current index is an uppercase vowel, and if so, it increments the count. Ultimately, the function returns the final count of uppercase vowels in even indices.