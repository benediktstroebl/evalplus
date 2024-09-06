```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len([x for x in txt if x.islower() and ord(x) % 2 == 0])
    return ans
```

The problem specification mentions that if there's no whitespace nor comma in the text, the function should return the number of lower-case letters with odd order in the alphabet. This kind of logic is usable when there's no well-defined "splitting points" in the text, and the text could be any value, like a numerical value. 

The function headed to that direction, assuming that if there's no commas and no whitespaces, the text is a single lower-case word consisting of letters with odd order, and thus returning the count of such letters.