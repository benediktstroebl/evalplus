```python
import re

def split_words(txt):
    lst = re.findall(r'\w+', txt)
    if len(lst) > 0:
        return lst
    else:
        commas = txt.count(',')
        if commas > 0:
            return txt.split(',')
        else:
            return len(txt.lower())%2==0
```

The code uses regular expressions with the re module to split the string into words using the `\w+` pattern, which matches one or more word characters (a word character in Python includes alphabets, digits, and underscores like in `a_1`). If the text doesn't contain any word characters, it checks if there are any commas, and splits the text into a list of words using the comma as a delimiter. If the text doesn't have any commas, it returns whether the number of lowercase letters is odd using the `len()` and `lower()` functions.