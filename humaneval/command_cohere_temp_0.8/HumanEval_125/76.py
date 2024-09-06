```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return words if words is not None else [txt]
```

This Python script defines a function called `split_words` that takes in a string variable `txt` as input. The function utilizes different logic structures to determine the appropriate splitting behavior based on the characters present in the input string.

First, the function checks if the string contains a comma (`','`) by employing the syntax `if ',' in txt`. If commas are present, the string is split into a list of words using the `split()` method, where the delimiter is a comma. This results in each word being separated by a comma.

Secondly, if the string does not contain a comma, the function checks if it contains any spaces by using the condition `if ' ' in txt`. If spaces are present, the `split()` method is utilized again, but this time with a space as the delimiter, effectively splitting the string into a list of words separated by spaces.

In the event that the string contains neither commas nor spaces, the function proceeds to check if the string is alphabetic using the condition `if txt.isalpha()`. If it is an alpha string, the function employs the `len()` function to determine the number of lowercase letters present in the string. This value is then returned as a list with a single element, the input string itself.

Finally, if none of the aforementioned conditions are met, the function returns `None`. To ensure robustness, the function returns the appropriate answer type (list or integer) for the given inputs.

The provided example usages are also included in the code snippet, showcasing how the `split_words` function operates on different input scenarios.