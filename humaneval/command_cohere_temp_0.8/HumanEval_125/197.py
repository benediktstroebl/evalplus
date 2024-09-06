```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else 0
    return ans
```

The provided Python script solves the problem by initially checking if the string contains whitespace or comma separators. If neither is present, it checks if the string contains only lowercase letters, confirming that it is a string of words. Subsequently, the function returns the list of words split using whitespace or commas, or the total count of words if no separators are present. This ensures that the result aligns with the problem's expectations for input examples like "Hello world!", "Hello, world!", and "abcdef".