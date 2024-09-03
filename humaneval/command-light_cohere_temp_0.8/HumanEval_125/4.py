Sure, here's a Python script with a self-contained function that splits a given string into words based on whitespace and punctuation:
```python
import re

def split_words(txt):
    return [w for w in re.findall('\\s+|\.,|-]', txt)]

# Test cases
assert len(split_words("Hello world!")) == 6
assert len(split_words("Hello,world!")) == 6
assert len(split_words("abcdef")) == 3
assert len(split_words("   abcdef  ")) == 3
assert len(split_words("(foo)123")) == 3
assert len(split_words("(foo bar)")) == 4
```
This script defines a function called **split_words**, which takes a string **txt** as input and returns a list of words from the string. The function uses the **re.findall** method to find all whitespace, comma, dot, or hyphen characters from the string.