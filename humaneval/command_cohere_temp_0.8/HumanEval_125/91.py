```python
def split_words(txt):
    ans = txt.split(",")
    if len(ans) > 0:
        return ans
    else:
        if ' ' in txt:
            return txt.split()
        else:
            return len(txt.lower())%2
```

The problem asks to return the list of words split on whitespace, if no whitespace exists in the text, it should split on commas. If no commas are found, return the number of lowercase letters with odd order in the alphabet. The provided solution uses Python's string methods to quickly check for the existence of whitespace and commas, returning the desired result without brute-forcing multiple conditions.