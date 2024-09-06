```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in string:
        index = alphabet.find(char) + 2 * 2 
        if index > 26:
            index -= 26
        encrypted += alphabet[index]

    return encrypted
``` 

This Python script defines a function `encrypt` taking a string as an argument and returning an encrypted string. The algorithm rotates the alphabet by 2 steps, multiplied by 2 places, and loops through the original string, converting each character to its new encrypted index. If the index is greater than 26, it wraps around by subtracting 26. The script provides a concise and readable solution to the problem.