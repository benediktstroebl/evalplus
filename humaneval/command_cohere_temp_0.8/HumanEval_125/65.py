```python
import re

def split_words(txt):
    if re.search(r'\s', txt):
        return txt.split()
    elif re.search(r',', txt):
        return txt.split(',')
    else:
        return len(list(filter(lambda c: ord(c) > 14 and ord(c) % 2 == 0, txt.lower())))
```

The problem is relatively straightforward. First, we check for the presence of whitespace with a regular expression. If whitespaces exist, we simply split the string into a list of words. If no whitespace is present, we check for commas, and if none are present, we calculate the number of letters with an even side in the alphabet. Notably, the alphabet has 26 letters, of which 26/2 = 13 have an even side. The remaining 13 letters have an odd side. Thus, we filter all letters with an even side and count them. The letter 'a' has a side of 0, 'b' has a side of 1 and so on. Finally, the function returns the count of these letters.