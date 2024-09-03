```python
def anti_shuffle(s):
    """
    anti_shuffle function takes a string and rearranges its characters based on ascending ASCII values.

    The string is split into individual characters and then each character's ASCII value is used to determine the next character to insert in the rearranged string.

    Returns the string of characters with the desired order.

    Example the string "Hello World!!!":
    anti_shuffle('Hello World!!!') == '!dlroWW W!!!'
    """
    Test cases
    """
    assert anti_shuffle("") == ""
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("!") == "!w!!"
    assert anti_shuffle("abc123") == "ab123"
    assert anti_shuffle("A12345") == "12345"
    assert anti_shuffle("abc123") == "bc123"
    assert anti_shuffle("") == ""
    assert anti_shuffle("aaaa") == "LKJSKM"
```