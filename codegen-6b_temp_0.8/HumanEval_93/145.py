
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
    s = []
    for ch in message:
      if ch.isalpha():
        code = ord(ch) - ord('a')
        code += 2
        if code > 25:
          code -= 26
        s.append(chr(code + ord('a')))
      else:
        s.append(ch)
    return ''.join(s)
    