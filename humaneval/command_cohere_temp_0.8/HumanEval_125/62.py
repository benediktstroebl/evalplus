```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans
```

The problem prompts to return the list of words split on whitespace if such whitespace exists. However, if no whitespace is present in the text, it should split on commas. In the case that both commas and whitespace are absent, the function should return the number of lowercase letters with even ordinal order in the alphabet (counting 'a' as 0, 'b' as 1, and so on). The provided code solves this problem by checking for the presence of spaces and commas, splitting the string accordingly. If neither whitespaces nor commas are found, it counts the number of lowercase letters with an even ordinal order and returns that count.