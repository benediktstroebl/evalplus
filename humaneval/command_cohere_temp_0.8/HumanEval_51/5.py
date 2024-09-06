Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both lowercase and uppercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. This approach ensures that all occurrences of vowels are removed while keeping non-vowel characters intact.

Here's an example usage:
```python
result = remove_vowels("abcdef")
print(result)  # Output: 'bcdf'
```

This will print 'bcdf' as the result of removing vowels from the string "abcdef".