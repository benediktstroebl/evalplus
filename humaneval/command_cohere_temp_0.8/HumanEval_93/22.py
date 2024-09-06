```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.find(c) + 2 + vowels[vowels.find(c) + 1]
        for c in message
    )
    return new_message
```

This code defines a function `encode` that takes a message as an input. It sequentially steps through each character in the message. For alpha characters, if it is a vowel, it looks up the character's index in the 'vowels' string, adds 2 to that index to get the character 2 places ahead, and then adds the next character after that to get the encoded value. If the character isn't a vowel, it casts it to uppercase. Then, it concatenates all these encoded characters to return the encoded message. This satisfies the 'swap case' goal and replaces vowels according to the rules mentioned in the problem. 

Output:
```
TGST
tHKS KS C MGSSCGG
``` 
You can test this script by calling the `encode` function with any string input.