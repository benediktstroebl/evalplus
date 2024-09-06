Here's a self-contained Python function that solves the markdown encoding problem you described:
```python
def encode_markdown(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_markdown(s: str):
    """
    takes as input string encoded with encode_markdown function. Returns decoded string.
    """
    expected input to be a string that was encoded using the encode_markdown function.
    """
    expected input, the output should be decoded markdown string.

Example usage:
```python
# Test function encode_markdown
print(encode_markdown("hello world!"))  # Output: '**,