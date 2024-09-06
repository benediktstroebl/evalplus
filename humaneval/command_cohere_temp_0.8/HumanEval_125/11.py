```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return words if words is not None else [txt]
```

This solution assumes that the text `txt` is already converted to a lowercase to make the letter counting case-insensitive. The `split()` method is used in a clever way to achieve the desired result, while taking into account different possible scenarios of whitespace and commas in the text. If none of these delimiters is present, it returns the length of the text if it consists only of lowercase letters, or `None` when the text is not convertible to lowercase or does not contain any letters. The final outcome is that the function will return `None` if `txt` does not consist of lowercase letters, and in this case, it is safer to return the original text as a single element in the list rather than returning `None` and risking a failure in the downstream processing that expects a list of words. 

**Note**: this approach assumes that the text input is already in lowercase as the built-in `isalpha()` function in Python does not account for case sensitivity, and the function counts the letters while ignoring the case.  If the input is not already in lowercase, you can use the `lower()` method to convert it before splitting or counting the letters, e.g.:
```python
def split_words(txt):
    words = txt.lower().split(',') if ',' in txt else txt.lower().split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return words if words is not None else [txt]
``` 

This modification allows the function to work case-insensitively and still converts the text to a list of words if it is possible, or returns the original text as a single element if the text does not contain any alphabetic characters.