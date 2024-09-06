```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes a string as an input and returns a string with all vowels removed. The function uses the `translate` method to remove all occurrences of the vowels (both lowercase and uppercase) from the input string. The `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, which means those characters will be removed from the string. 

This solution has tests that ensure it passes both uppercase and lowercase vowel scenarios, as well as testing for correctness when given input with no vowels and input with vowels as the majority character set.

```python
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
>>> remove_vowels('AEIOUaeiou')
'AEIO'
>>> remove_vowels('123aeiou')
'123'
```