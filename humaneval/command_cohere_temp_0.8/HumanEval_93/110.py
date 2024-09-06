```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(ch.swapcase() if ch.isalpha() and ch not in vowels 
                           else (vowels.find(ch) + 2) % 26 + vow.lower() 
                           for ch in message)
    return new_message
```