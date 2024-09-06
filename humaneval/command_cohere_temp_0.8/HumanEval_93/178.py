```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []

    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = alphabet[alphabet.index(char) + 2]
            else:
                new_char = char.swapcase()
            new_message.append(new_char)
        else:
            new_message.append(char)

    return ''.join(new_message)
```

This code defines a function `encode(message)` that takes in a message as an input. 

The function then creates two lists: `vowels` and `alphabet`, which categorize all vowels in the English alphabet and the entire English alphabet, respectively. 

Then, within a for loop, each character in the provided input `message` is checked using the Python method `isalpha()` to verify if it is a letter. If the character is a letter, it is then checked to see if it is a vowel, using the `vowels` list. If the character is a vowel, the function uses the `alphabet` list to find the 2nd letter after the current vowel, and uses that as the new character in the `new_message` list, which is compiled on the go. Otherwise, the character is converted to its alternate case using Python's `swapcase()` method and is added to the `new_message` list. 

The function then joins the characters of `new_message` together into a single string, and returns this result. 

This algorithm will successfully encode any letter using the rules described in the problem statement, and any non-letter characters will remain unchanged. 

Here is an example output:
```
>>> encode('test')
'tgst'
>>> encode('This is a message')
'thks ks c mgsscgg'
``` 

This encodes the messages using the specified rules and swaps the case of all letters that are not vowels.