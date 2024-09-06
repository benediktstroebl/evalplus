```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes all vowels, both lowercase and uppercase, from the given text. You can test this script with the provided tests and see that it correctly solves the problem. Adjust the tests or code if needed to fit specific requirements. Feel free to ask if you have further questions or need assistance with any other topics!