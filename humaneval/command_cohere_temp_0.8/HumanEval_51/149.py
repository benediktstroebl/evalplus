```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. The function utilizes the `translate` method with custom translations to eliminate all vowels (both lowercase and uppercase) from the input text. The str.maketrans method is used to create a translation table that maps each character in the vowels string to `None`, effectively removing them from the text while leaving other characters intact. The function returns the modified text without vowels. 

This solution is encapsulated within a function, making it both self-contained and readily available for use in various parts of code that require removing vowels from text. 

Note: The solution utilizes Python's translation mechanism, which is a powerful method for conducting character-based operations on strings.