```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function called `remove_vowels` that takes one argument, `text`. It creates a translation table using `str.maketrans("", "", vowels)` that maps each vowel (uppercase and lowercase) to `None`. Then, the `translate` method is used to remove all vowels from the text. The `translate` method removes all characters that are mapped to `None` in the translation table. 

This method ensures that all instances of vowels (uppercase and lowercase) are removed from the input text. The resulting text without vowels is then returned. 

The expected behavior of the function is described using Python's `assert` statements. These statements compare the actual output from each example to the expected output and check if they are equal. If the outputs are unequal, the test fails and this is indicated to the user. 

This way, you can validate that the function performs as expected on a variety of inputs.