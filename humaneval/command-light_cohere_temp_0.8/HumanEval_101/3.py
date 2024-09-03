```python
def words_string(s):
    """
    Splits the input string into an array of words.
    Returns: array of words.
    """
    words separated by commas or spaces
    """
    return s.split(', ')
split(' ')

def test_words_string():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("abc123!") == ["abc", "123"]
    assert words_string("🏠️➉⌂") == ["🏠️", "➉", "⌂"]
```