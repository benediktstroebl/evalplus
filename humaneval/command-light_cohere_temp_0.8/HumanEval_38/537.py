```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    common cases:
    if input string is 'abc...'
      return 'abc...'
    elif input string is '...a'  
      return '...a'
    elif input string is '...b'
      return '...b'
    elif input string is '...c'
      return '...c'
    elif input string is '...d'
      return '...d'
    elif input string is '...e'
      return '...e'
    elif input string is '...f'
      return '...f'
    elif input string is '...g'
      return '...g'
    elif input string is '...h'
      return '...h'
    else:
      return 'Invalid input'
```