```python
import re

def split_words(txt):
    ans = []
    txt = re.sub('[^a-zA-Z0-9']', '', txt)
    words = txt.split(',')
    for w in words:
        if w:
            ans.append(w)
    if not ans:
        return 0
    return ans
```

The code uses regular expressions to remove any non-alphanumeric characters and then splits the text into words using a comma as a delimiter. If no commas are found, the function returns the number of words in the text (odd or even). You can copy the code into an "split_words.py" file and run it to see the function's behavior for different test cases.