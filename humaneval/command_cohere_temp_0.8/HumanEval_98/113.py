```python
def count_upper(s):
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This approach leverages string slicing and a loop that iterates over the string at intervals of 2 indices. The function then checks if each character at these even indices is an uppercase vowel, counting them using a predefined list of uppercase vowels. The function finally returns the count of uppercase vowels in the even indices of the string.

Note that this solution assumes the input string contains only ASCII characters, and it might not work as expected with other character sets. If supporting non-ASCII characters is necessary, additional code would be required to handle them appropriately.