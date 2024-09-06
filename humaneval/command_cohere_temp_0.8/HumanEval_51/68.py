Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans()`. This approach ensures that all occurrences of vowels are removed while keeping non-vowel characters intact.

The expected outcome for each test case is:
- `>> remove_vowels('')`: ``
- `>> remove_vowels("abcdef\nghijklm")`: 'bcdf\nghjklm'
- `>> remove_vowels('abcdef')`: 'bcdf'
- `>> remove_vowels('aaaaa')`: ''
- `>> remove_vowels('aaBAA')`: 'B'
- `>> remove_vowels('zbcd')`: 'zbcd'

This approach is more concise and efficient than the previous ones, and it guarantees the correct removal of vowels from the input text.