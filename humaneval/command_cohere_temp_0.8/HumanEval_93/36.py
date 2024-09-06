```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''.join(alphabet[alphabet.index(c) + 2] if c in vowels else c for c in message)
    return res.swapcase()
```