```python
def encrypt(s):
    """Encrypt a string with a twice-doubled alphabet shift.

    Args:
        s (str): String to be encrypted.

    Returns:
        str: Encrypted string.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            pos = alphabet.find(char)
            encrypted += alphabet[(pos - shift) % 26]
        else:
            encrypted += char
    return encrypted
```