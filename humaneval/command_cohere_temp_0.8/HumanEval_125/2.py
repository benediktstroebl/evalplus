```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return ans
```

The problem asks for a list of words split on whitespace, if no whitespace exists in the text, it suggests splitting on commas. If commas and whitespace are absent, the function is asked to return the total count of lowercase letters with an odd order in the alphabet. The function checks for the existence of commas and spaces using the `in` operator, assigns the answer as a list split on commas or whitespace, and if neither is present, checks if the string contains only lowercase letters using the `isalpha()` method, finally, if the string contains only lowercase letters, it returns the total count of letters with an odd order.