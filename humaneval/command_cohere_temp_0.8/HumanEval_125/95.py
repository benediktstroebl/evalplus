```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans
```

The function takes an input string and checks if the string contains spaces or commas to split it into a list of words. If there are no spaces or commas, it counts the number of lowercase letters with an even decimal value and returns the result. The function returns the appropriate response based on the above conditions.