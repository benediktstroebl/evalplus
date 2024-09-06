Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))
```
This removes all vowels, both uppercase and lowercase, from the text using the `translate` method and the `maketrans` function. It returns the modified text without vowels. 
The expected behavior for the tests provided is:
```
''
bcdf\nghjklm'
'bcdf'
''
'B'
'zbcd'
```
This approach makes use of string translation, a technique that has good performance and robustness for various cases. It is also applicable for handling other types of characters or special sequences through the customization of the translation dictionary.