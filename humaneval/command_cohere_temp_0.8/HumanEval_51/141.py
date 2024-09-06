Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return text.translate(str.maketrans("", "", vowels))
```
This removes all vowels, both uppercase and lowercase, from the text using the `translate` method and the `str.maketrans` function. It returns a new string where all occurrences of vowels have been removed. The tests provided match the behavior of the script. 
```python
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```
Feel free to modify the script to suit your needs or ask if you have any questions!