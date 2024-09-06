def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(ch.swapcase() if ch.isalpha() and ch not in vowels 
                           else vowels.index(ch) + 2 + vowels[vowels.index(ch) + 1] 
                           for ch in message)
    return new_message