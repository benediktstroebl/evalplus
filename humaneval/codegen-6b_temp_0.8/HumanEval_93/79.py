
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # import string
    # new_alphabet = string.ascii_letters
    # v_count = 0
    # for i in new_alphabet:
    #     if i in 'aeiou':
    #         v_count += 1
    # print('vowels:', v_count)
    # alphabet = string.ascii_letters + string.digits + string.punctuation
    # key_map = dict(zip(alphabet, alphabet[-2:] + alphabet[:-2]))
    # return ''.join(key_map.get(i, i) for i in message)
    #
    # return ''.join(new_alphabet[(new_alphabet.index(c) + 2) % len(new_alphabet)] if c in new_alphabet else c for c in message)
    #
    # return ''.join(key_map[letter] if letter in key_map else letter for letter in message)

    # I am VERY STUPID for what I'm doing here, but it was a fun challenge.
    # 
    return message.upper().translate(str.maketrans('aeiou', '123'))

