Here's a Python script with a function that solves the problem as described in the code block:
```python
def count_upper(s):
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a list `upper_vowels` to store the uppercase vowels and a `count` variable to keep track of the count. The function then iterates through the string at even indices using a `for` loop and checks if the character at that index is an uppercase vowel using the `isupper()` method and the membership test `s[i] in upper_vowels`. If both conditions are met, it increments the count. Finally, it returns the total count.