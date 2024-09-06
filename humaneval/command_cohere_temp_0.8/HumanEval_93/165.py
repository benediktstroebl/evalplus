```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''.join(alphabet[alphabet.index(c) + (c in vowels) * 2] for c in message if c in alphabet)
    return encoded
```

This Python script defines a function `encode` that takes a message as an input parameter. The function utilizes two lists: `vowels` for all vowel characters in the English alphabet and `alphabet` for the entire English alphabet. The `encoded` string is created by iterating through each character in the input `message`. For each character, if it exists in the alphabet, its position is determined, and it's appended to the `encoded` string with consideration of whether it is a vowel. The resulting `encoded` message is then returned as the result. 

Is there anything else I can help you with? Feel free to specify the desired code blocks or provide any descriptions, and I'll do my best to assist you.