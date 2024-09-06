Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above code defines a function remove_vowels that takes a string text as input and returns a string without any vowels. The function uses the translate method to remove vowels. The str.maketrans method creates a translation table that maps each character in the string to itself (this will effectively remove the characters if they are present in the string), and the translate method is used to apply this translation.

Here is a simpler solution:
```python
def remove_vowels(text):
    return text.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
```

And another solution is:
```python
def remove_vowels(text):
    return text.translate(str.maketrans("", "", "aeiouAEIOU"))
```

All of these functions can be tested in the same way as the provided tests to ensure they perform as expected.