```python
import re

def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    no_space = re.findall(r'\W+', txt)
    if no_space:
        return txt.split(',')
    no_comma = re.findall(r'\w+,\w+', txt)
    if no_comma:
        return [txt]
    else:
        return len(re.findall(r'(.)\1+', txt))
```

The function utilizes regular expressions to solve the problem rely on the following patterns:
1. `\W+`: This matches strings that contain none or several whitespace characters (space, tab, newline, etc.).
2. `\w+,\w+`: This matches strings that contain one or more word characters (letters, digits, and underscores) followed by a comma followed by one or more word characters.
3. `(.)\1+`: This matches strings that contain pairs of identical characters multiplied indefinitely. This will match all characters that have an odd number of occurrences in the string since after matching a character and counting it, the subsequent character will be the same and the count incremented.

The function iterates through these patterns and returns a list of words if whitespace or commas are present, or the number of characters with odd occurrences if neither are present.

The unit tests would look like this:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3 
    assert split_words("this_is_a_test") == "this_is_a_test"
    assert split_words("abc") == "abc"
    assert split_words("abc,") == ["abc"]
    assert split_words("abccode") == ["ab", "cc", "ode"]
    assert split_words("abccode,") == ["ab", "cc", "ode"]
    assert split_words("hello world") == ["hello", "world"]
    assert split_words("hello,,world") == ["hello", ",", "world"]
    assert split_words("hello world,") == ["hello", "world"]
    assert split_words("hello,,") == ["hello", ",", ","]
    assert split_words("abc,def") == ["abc", "def"]
    assert split_words("abc,def,ghi") == ["abc", "def", "ghi"]
    assert split_words("abc,def,,ghi") == ["abc", "def", ",", "ghi"]
    assert split_words("abcdefghijklmnopqrstuvwxyz") == 26
```