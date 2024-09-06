```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes a single argument, `text`. It returns the provided text without any vowels, both uppercase and lowercase, present in it. This is achieved using the `translate` method, where `str.maketrans("", "", vowels)` creates a translation table that maps each vowel to `None`, effectively removing them from the text. 

This code is concise and achieves the goal effectively, providing a straightforward way to remove vowels from a given text. It can be called like this:
```python
print(remove_vowels("Hello, World!"))
```
```bash
Hll, Wrd!
```