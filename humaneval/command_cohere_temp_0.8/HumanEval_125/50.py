```python
import re

def split_words(txt):
    lst = re.findall(r'\w+', txt)
    if len(lst) > 0:
        return lst
    else:
        comma_lst = txt.split(',')
        if len(comma_lst) > 1:
            return comma_lst
        else:
            return len(txt)
```
The code uses a regular expression `\w+` to match words regardless of whitespace, and commas as a fallback. The use of `re.findall` guarantees a list is formed even if there are no matches. If there are no words nor commas, the code returns the length of the string, as the last line of defense. 

## Testing

```python
# test split_words("Hello world!")
assert split_words("Hello world!") == ["Hello", "world!"]

# test split_words("Hello, world!")
assert split_words("Hello, world!") == ["Hello", "world!"]

# test split_words("abcdef")
assert split_words("abcdef") == 3

# test split_words("abc")
assert split_words("abc") == ["abc"]

# test split_words("abcf")
assert split_words("abcf") == 2

# test split_words("abc,def")
assert split_words("abc,def") == ["abc", "def"]

# test split_words("This has, comma's!")
assert split_words("This has, comma's!") == ["This", "has", "comma's!", ""]

# test split_words("This has no commas or spaces")
assert split_words("This has no commas or spaces") == ["This", "has", "no", "commas", "or", "spaces"]
```