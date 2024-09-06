def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(chr(ord(c) + (ord(vowels.find(c)) - 2) % 26) if c in vowels else c for c in message)
    return new_message.swapcase()