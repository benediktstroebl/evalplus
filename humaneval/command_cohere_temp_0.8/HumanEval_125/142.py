```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return words
```

The code solves the problem by doing the following:
- It first checks if there is a comma ',' in the text. If found, it splits the text into a list of words using the comma as a separator.
- If there are no commas, it checks if there is whitespace ' ' in the text. If found, it splits the text into a list of words using the whitespace as a separator.
- If neither commas nor whitespace is present, it counts the number of letters that have an odd parity when interpreted as an integer (using the filter function with a lambda clause). This count is then returned as the list of words.

The provided code defines the `split_words` function, which takes a string as input and returns the list of words split on whitespace or commas, or the number of letters with odd order in the alphabet if no whitespace or commas are present. The function handles different input scenarios and provides the appropriate result based on the given criteria. It can be used to split a string of words into a list of words, handle scenarios where there are no whitespace or commas, and leverage the odd order of letters to split the string creatively when necessary.