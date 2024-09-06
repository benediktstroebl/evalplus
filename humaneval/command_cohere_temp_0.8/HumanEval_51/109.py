```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes a single argument, `text`, which is a string. Within the function, it creates a translation table using the `str.maketrans()` method, which maps each character in the string `vowels` to `None`, effectively removing them from the text. The `translate()` method is then used to apply this translation to the input text, removing all vowels from it. The function returns the modified string without vowels. 

This solution is concise and achieves the goal of removing vowels from the input text, and is compatible with the given tests. 

The script can be accompanied by a markdown block:
```
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

# Testing the function
print(remove_vowels("abcdef"))           # Outputs 'bcdf'
print(remove_vowels("aaaaa"))           # Outputs ''
print(remove_vowels("aaBAA"))           # Outputs 'B'
print(remove_vowels("zbcd"))            # Outputs 'zbcd'
print(remove_vowels("abcdef\nghijklm")) # Outputs 'bcdf\nghjklm'
```
```

This would provide a complete solution to the problem that is self-contained within the markdown code block.