Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above method uses the `translate` method with `str.maketrans("", "", vowels)` to remove all vowels from the string. This approach works on both lowercase and uppercase vowels and returns the modified string. You can test it by calling the function with different input strings as demonstrated in the provided docstring. The expected output for each test case is also shown in the docstring. 
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

>> remove_vowels('')
''
>> remove_vowels("abcdef\nghijklm")
'bcdf\nghjklm'
>> remove_vowels('abcdef')
'bcdf'
>> remove_vowels('aaaaa')
''
>> remove_vowels('aaBAA')
'B'
>> remove_vowels('zbcd')
'zbcd'
```