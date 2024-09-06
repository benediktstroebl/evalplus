```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != [''] else len(min(txt.lower(), key=lambda x: (x.count('z'), x.count('a'))))
```

The problem prompts the function `split_words` to parse a string and return a list of its words if it contains at least a whitespace, otherwise, it should split the string on commas. Think of a scenario where a string contains no spaces nor commas, in this case, the function returns the number of lowercase letters with odd alphabet order positions. This condition verifies the functionality of the `split` methods on whitespace and commas and uses a `min` comparison with a key function to count the number of letters with an odd alphabet position, in case the string contains only uppercase letters, it will not return a list of empty strings.