```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    is! value of the test function."""

Test case 1:

> >> test_encode_cyclic("abcabc")
> "cobe..."

Test case 2:

>> >> test_encode_cyclic("doitondoit")
>> "dlrodcdo"

Test case 3:

>> >> test_encode_cyclic("letemlletem")
>> "tkteaek"

Test case 4:

>> >> test_encode_cyclic("hello world")
>> "ehlowvvld"

Test case 5:

>> >> test_encode_cyclic("hello )
>> "elodrfh"

Test case 6:

>> >> test_encode_cyclic("hello world")
>> "elodrfhv"

Test case 7:

>> >> test_encode_cyclic("hell)
>> "elodrfh"

Test case 8:

>> >> test_encode_cyclic("hello he")
>> "elodrfh"

Test case 9:

>> >> test_encode_cyclic("hello ,world")
>> "elodrfh,"