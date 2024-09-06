Here's the Python code to solve the problem:
```python
def count_upper(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and s[i] in 'AEIOU':
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a for loop to iterate through each character in the string, checks if the index is even and the character is an uppercase vowel, and increments the count if both conditions are met. The result is the total count of uppercase vowels in even indices.