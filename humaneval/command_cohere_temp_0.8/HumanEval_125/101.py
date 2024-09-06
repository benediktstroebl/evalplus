```python
import re

def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]+'))
    if len(ans) > 0:
        return ans
    else:
        return len(re.findall(r'[a-z]', txt)) % 2
```

The Python script uses a regular expression (re) to match any whitespace (space or comma) in the input text and uses the split() method to split the text into a list of words. If no whitespace is found, the script returns the number of lowercase letters with odd order in the alphabet. The re.escape() function is used to escape any special characters in the regular expression, and the re.findall() function is used to count the number of lowercase letters in the text. Finally, the len() function is used to get the length of the list and the modulus operator % is used to determine whether the length is odd.