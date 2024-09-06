```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1 == ord(c), txt.lower())))
    return ans
```

The problem solver takes into consideration the priority of splitting between whitespace or comma separated values. An edge case, in which there are no whitespaces or commas, the function also accounts for counting odd numbered letters in the alphabet.