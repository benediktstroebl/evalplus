```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) % 2 == 0, txt.lower())))
    return ans
```

The function takes an input string and checks if the string contains spaces or commas to split it into a list of words. If there are no spaces or commas, it counts the number of lowercase letters with an even alphabetical order. The number of such letters is then returned as the output. The function is self-contained and can be executed directly to produce the desired results.