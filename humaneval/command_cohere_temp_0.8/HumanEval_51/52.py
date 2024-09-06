Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function called `remove_vowels` that takes a single argument, `text`, which is a string. Inside the function, it defines a string called `vowels` that contains all possible vowels, both lowercase and uppercase. It then uses the `translate` method to remove all vowels from the `text` string by using `str.maketrans("", "", vowels)` to create a translation table that maps every character in the `vowels` string to `None`.

Here is an example to demonstrate the function:
```python
>>> remove_vowels("abcdef")
'bcdf'
```

And here is the remainder of the code block with tests to verify the function:
```python
>>> remove_vowels('')
''
>>> remove_vowels("abcdef\nghijklm")
'bcdf\nghjklm'
>>> remove_vowels('abcdef')
'bcdf'
>>> remove_vowels('aaaaa')
''
>>> remove_vowels('aaBAA')
'B'
>>> remove_vowels('zbcd')
'zbcd'
```

This also demonstrates that the problem statement's test cases are integrated into the code block and that the function passes them all, proving its validity.  This function will remove all vowels, both lowercase and uppercase, from any string it is given as input.  It is also worth noting that using `str.translate()` method is more efficient and recommended for production code compared to using a list comprehension approach.  This approach also makes the code more readable and easier to understand.