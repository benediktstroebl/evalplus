```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return ans
```

The code solves the problem by performing the following steps:
1. Checks if there is a comma ',' in the text and splits the text into a list using ',' as the delimiter.
2. If there are no commas, it checks if there is whitespace ' ' in the text and splits the text into a list using ' ' as the delimiter.
3. If both commas and whitespaces are not present in the text, it converts the text to lowercase, counts the number of letters with an odd parity when interpreted as integers (using the filter function with a condition 'lambda c: ord(c) ^ 1'), and converts the count to a list.

The provided code defines a function `split_words` that takes a string as input and returns the appropriate response based on the conditions outlined in the problem statement.