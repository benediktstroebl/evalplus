```python
import re

def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]'))
    if len(ans) > 0:
        return ans
    else:
        return len(re.findall(r'[a-z]', txt)) % 2
```

The Python script takes advantage of regular expressions via the `re` module to efficiently split the string `txt` into a list of words. It utilizes the `re.escape()` function to escape any whitespace or comma characters in the text, ensuring they are treated as literal characters when splitting the text.

The `split()` function is then used to split the text into a list of words based on the escaped characters '[ ,]'. This effectively separates the text into words using whitespace or commas as separators, depending on which ones are present in the text.

If the split operation returns an empty list, meaning there are no words in the text, the function innovatively utilizes another regular expression, `re.findall(r'[a-z]', txt)`, to count the number of lowercase letters in the text. The modulo 2 operation (`% 2`) is then applied to this count to determine whether the number of lowercase letters has an odd or even count.