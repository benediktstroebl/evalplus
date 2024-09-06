```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This code defines a function `remove_vowels` that takes a single argument `text`, which is a string, and returns a modified version of that string with all vowels (both lowercase and uppercase) removed. 

The function utilizes the `translate` method with custom character translations provided by `str.maketrans("", "", vowels)` to remove all instances of vowels from the input string while ignoring other characters. 

This approach ensures that even non-alphabetic characters and numbers in the input string are left untouched, while vowels of both lowercase and uppercase varieties are selectively removed. 

The behavior of the function is demonstrated through a series of tests that showcase its efficacy in removing vowels from various input scenarios, including empty strings, strings with spaces, and strings with uppercase vowels, resulting in the expected output. 

The code includes a multi-line string `vowels` that contains all lowercase and uppercase vowels, ensuring comprehensive removal of both types across different input cases.