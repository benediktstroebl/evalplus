def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(chr(ord(c) + (ord(c) in vowels and ord(vowels[abs(ord(c) - 2) - 96]) or ord(c)) - 96) for c in message)
    return new_message.swapcase()