Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. It supports various edge cases like handling empty strings, multiple lines, and preserving non-vowel characters.

Here's an example of how you can use this function:
```python
result = remove_vowels("abcdef")
print(result)  # Output: 'bcdf'

result = remove_vowels("aaaaa")
print(result)  # Output: ''

result = remove_vowels("aaBAA")
print(result)  # Output: 'B'

result = remove_vowels("zbcd")
print(result)  # Output: 'zbcd'
```

The expected output is:
```
bcdf

```

```
```
B

zbcd
```

This updated version handles all test cases, including empty strings, multiple lines, and preserving non-vowel characters.