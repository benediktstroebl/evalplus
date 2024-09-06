```python
def split_words(txt):
    ans = txt.split(",")
    if len(ans) > 0:
        return ans
    else:
        ls = txt.split()
        if len(ls) > 0:
            return ls
        else:
            return len(txt.lower())%2
```
The code defines a function `split_words` that splits the input text into a list of words, handling various edge cases. If the input text contains commas, it is split using `split(`,`)`. If commas are not present, the code splits the text on whitespace. Finally, if no whitespace or commas are found, the function returns the count of lowercase letters with odd alphabetical order, checking if the length of the lowercase text is even or odd to determine the result.