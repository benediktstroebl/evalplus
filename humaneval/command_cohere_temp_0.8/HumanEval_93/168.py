```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''

    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += alphabet[alphabet.find(char) + 2]
            else:
                encoded += char.swapcase()
        else:
            encoded += char

    return encoded
```

The provided Python script defines a function called `encode` that takes a message as input. Within the function, it initializes two strings: `vowels` contains all the vowels in the English alphabet in lowercase and uppercase, and `alphabet` is a string containing all letters in the English alphabet in lowercase and uppercase.

It then creates an empty string `encoded` to store the encoded message. The function iterates through each character in the input `message`. For each character, it checks if it is a letter using the `isalpha()` method. 

If the character is a vowel, it appends to `encoded` the letter that is two positions ahead of the original vowel in the `alphabet` string. This essentially maps each vowel to a different letter. For example, 'a' becomes 'c', and 'A' becomes 'C'.

If the character is not a vowel, it checks if it is a letter and performs a swapcase, which swaps the case of the letter. This is accomplished by first converting the character to a lowercase letter and then appending it to `encoded`.

Finally, if the character is not a letter at all, it appends the character to `encoded` as is, regardless of its type. This is because the code specifically excludes these non-letter characters from any encoding transformation.

The output of this function is the `encoded` string, which is the message transformed as per the requirements of the prompt.