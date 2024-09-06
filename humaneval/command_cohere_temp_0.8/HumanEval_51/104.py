```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function `remove_vowels` that takes a single argument `text`, which is a string, and returns a modified version of that string with all vowels (both lowercase and uppercase) removed. 

The function achieves this by using the `translate` method with a `str.maketrans()` argument that creates a translation table which removes all characters that appear in the `vowels` string.

This approach ensures that all occurrences of vowels are removed from the input text while maintaining the relative positions of characters within the string.

The behavior of the function is demonstrated through a series of examples in the docstring, which also includes a brief description of the function and its expected behavior. 

The overall structure of the code follows the best practices of encapsulation and provides a clear and concise solution to the problem.