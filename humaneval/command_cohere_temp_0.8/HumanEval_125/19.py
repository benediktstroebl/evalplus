```python
import re

def split_words(txt):
    spaced = re.findall(r'\w+|[,\s]', txt)
    if len(spaced) == 1 and ',' not in txt:
        return len(txt.lower()) - sum(1 for c in txt if c != ' ')
    return spaced
```

The code uses a RegEx module to find all words or comma-separated parts of the text `txt`. If the text consists of one word and no commas, the function additionally checks if there are spaces in the text and calculates the answer counting the vowels. In any other case, it simply splits the text by whitespace or commas.