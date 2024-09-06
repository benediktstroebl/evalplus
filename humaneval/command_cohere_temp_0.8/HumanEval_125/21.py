```python
def split_words(txt):
    ans = txt.split(",")
    if len(ans) == 1:
        if " " in txt:
            ans = txt.split(" ")
        else:
            ans = len(list(filter(lambda x: x % 2 == 0, txt)))
    return ans
```

The problem asks us to return a list of words split on whitespace, if no whitespace exists in the text we should split on commas. In the event of both commas and whitespaces not being present in the text, we are asked to return the number of lower-case letters with odd order in the alphabet. To achieve this we attempt to split the text using whitespace, if this fails we attempt to split using commas, and in the event of both of these failing we iterate over every character in the string filtering out even letters and adding 1 to a counter.