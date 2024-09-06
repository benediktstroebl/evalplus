Here's the Python code to solve the problem:
```python
def count_upper(s):
    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a dictionary `upper_vowels` to store the uppercase vowels 'A', 'E', 'I', 'O', and 'U'. The function then iterates through the string in steps of 2 (i.e., even indices) using a loop with the range clause `range(0, len(s), 2)`. For each iteration, it checks if the character at that index is uppercase and a vowel. If both conditions are met, it increments the count. Finally, the function returns the total count of uppercase vowels in even indices.