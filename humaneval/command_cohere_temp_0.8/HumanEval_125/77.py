```python
import re

def split_words(txt):
    if re.findall(r'\s+|\,', txt):
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return len(list(filter(lambda x: x % 2 == 1, map(lambda x: ord(x.lower()) - 96, txt))))
```

The problem prompts us to extract words from a string, considering special cases with whitespace and commas. For instances with whitespace, we use `.split(' ')` to conventionally split; whereas, for instances with commas, we employ `.split(',')` to segregate words. In both cases, we return the list of words. For texts devoid of whitespace or commas, we leverage the re module to affirmatively ascertain the absence of whitespace or commas. We then utilize the `filter` and `map` functions to determine the count of lowercase letters with an odd number of occurrences, attributable to their position in the alphabet. This number corresponds to the count of words we would have encountered. 

The provided solution adheres to the problem's criteria and assumes a string `txt` that contains a multitude of words that are to be extracted under various conditions. 

The function beneath can be embedded in a Python script for standalone execution, as per the problem's stipulation of a self-contained solution. 

To ensure the function's correctness, you can incorporate tests to validate its behavior across diverse scenarios. Here's an example:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("This is a test with whitespace") == ["This", "is", "a", "test", "with", "whitespace"]
    assert split_words("This is a test with, comma") == ["This", "is", "a", "test", "with", "comma"]
    assert split_words("Lowercase letters: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z") == [
        "Lowercase", "letters:", "a", ",", "b", ",", "c", ",", "d", ",", "e", ",", "f", ",", "g", ",", "h", ",", "i",
        ",", "j", ",", "k", ",", "l", ",", "m", ",", "n", ",", "o", ",", "p", ",", "q", ",", "r", ",", "s", ",", "t",
        ",", "u", ",", "v", ",", "w", ",", "x", ",", "y", ",", "z"
    ]
```

These tests aim to evaluate the function's performance under different scenarios. 

The `re.findall(r'\s+|\,', txt)` utilizes the regular expression `\s+` to match one or more whitespace characters and `\,` to match a comma. The `filter(lambda x: x % 2 == 1, map(lambda x: ord(x.lower()) - 96, txt))` expression, through `filter`, eliminates letters with an even number of occurrences, while `map` decreases each letter to its corresponding position in the alphabet.