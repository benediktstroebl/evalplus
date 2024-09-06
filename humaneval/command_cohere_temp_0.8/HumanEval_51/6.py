Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function `remove_vowels` that takes a string text as an input and returns a string without any vowels. The function uses the `translate` method to remove vowels. The `str.maketrans()` method is used to create a translation table that maps each character in `vowels` to `None` and `""` to `None`, effectively removing any occurrences of vowels.

Here is an example output of the function:
```
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```

The example tests cover different scenarios to ensure the function correctly removes vowels from various input strings.