```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                offset = ord('a') if char in 'aeiou' else ord('A')
                new_message.append(alphabet[offset + 2 + (ord(char) - offset) % 26])
            else:
                new_message.append(char.swapcase())
        else:
            new_message.append(char)
    
    return ''.join(new_message)
```

The provided Python script offers a function named `encode` designed to transform a given message in a distinctive manner as described in the problem statement. This function takes a single argument, `message`, and encapsulates each character of this input according to its characteristics.

For alphabetic characters, it undergoes a dual transformation: first, it swaps the case of the characters, converting uppercase to lowercase and vice versa. Secondly, it replaces vowels with characters that are 2 places ahead of them in the English alphabet. The logic behind this vowel substitution is embedded in the `if char in vowels:` condition. Specifically, it checks if the character is among the vowels 'aeiouAEIOU'. If the character is a vowel, it calculates the offset - the difference between the ASCII value of the character and the first letter of the alphabet. This offset is used to determine the new character by adding 2 and performing a modulo 26 operation to ensure the wrap-around of the alphabet. This modified character is then appended to the `new_message` list.

Non-alphabetic characters, such as punctuation, spaces, or numbers, are spared from this transformation and directly added to the `new_message` list in their original form.

Lastly, the function concatenates all elements in the `new_message` list to produce the final encoded result, which is then returned.