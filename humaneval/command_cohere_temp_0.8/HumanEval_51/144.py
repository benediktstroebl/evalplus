Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above method uses the `translate` method to remove vowels from the text. The `str.maketrans()` method is used to create a translation table that removes the vowels, and these two steps are encapsulated in the `remove_vowels` function. You can use this function to remove vowels from any string input. 

Here is an example output of the function:
```
remove_vowels('abcdef')
'bcdf'
```
```
remove_vowels('aaaaa')
''
```
```
remove_vowels('aaBAA')
'B'
```
```
remove_vowels('zbcd')
'zbcd'
```