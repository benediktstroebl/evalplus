Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and a translation table created with `str.maketrans`. This approach ensures that all possible vowels, both lowercase and uppercase, are removed from the text.

Here's an example usage of the function:
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

The expected output for each test case is as follows:
```
bcdf

```
```
''

```
B

```
zbcd
```
```
These results are consistent with the test cases provided in the initial prompt. The function removes vowels from the input text, leaving only consonants and other characters untouched. Feel free to use this solution or modify it as needed for your purposes. If you have any more questions or need further assistance, please don't hesitate to ask! Let me know if you would like to delve deeper into any related topics or understand other coding problems you may be encountering.