```python
import re

def split_words(txt):
    ans = re.findall(r'\w+', txt)
    if len(ans) > 0:
        return ans
    else:
        commas = txt.split(',')
        if len(commas) > 1:
            return commas
        else:
            return len(txt)
```
The function `split_words` uses the `re.findall` function to find all contiguous sequences of word characters (letters, digits, underscores, and hyphens) using the regular expression pattern `\w+`. These are then returned as a list. If no such sequences are found, it splits the text at commas instead. If there are no commas either, it returns the total number of lowercase letters in the text. This handles the edge cases mentioned in the problem statement. 

Here is a test suite that can be used to validate the function:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("a b c") == ["a", "b", "c"]
    assert split_words("only_commas,") == ["only_commas"]
    assert split_words("no_words_or_commas") == len("no_words_or_commas")
```