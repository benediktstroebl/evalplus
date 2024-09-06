Here's a Python script that contains a function to solve the problem as specified in the code block:
```python
def count_upper(s):
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It uses a list `upper_vowels` to store the uppercase vowels and uses a `for` loop to iterate through the string at even intervals, checking if the character is uppercase and a vowel. The result is the count of such characters.

The expected behavior for the provided tests is:
1. `count_upper('aBCdEf')` should return `1` since 'E' is the only uppercase vowel in an even index.
2. `count_upper('abcdefg')` should return `0` as there are no uppercase vowels in even indices.
3. `count_upper('dBBE')` should return `0` as although there are uppercase vowels, they are not in even indices.

This solution is efficient and straightforward in calculating the count of uppercase vowels in even indices of a given string.