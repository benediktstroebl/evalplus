```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else 0
    return ans
```

This code defines a function `split_words` that splits the input text into a list of words based on whitespace or comma separation. If the input contains neither whitespace nor commas, it checks if it's a single word containing only lowercase letters, in which case it returns the length of the word (calculated using the `len` function), as specified in the prompt. This way, the function handles different possible scenarios for the input text.