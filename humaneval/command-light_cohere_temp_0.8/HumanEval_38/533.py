```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g if len(g) == 3 else g[1:] + g[0])

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    by reversing elements.
    """
   
    also checks that the decoded string is not a palindrome.
    """
    also has a test if the decoded string has a length greater than one, it will throw an error.
    """
return s if s.haslen() > 1 else s[-1:]