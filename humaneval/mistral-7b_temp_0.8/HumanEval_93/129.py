
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

    #coding:utf-8
    # 1. 将字母转换为大写 2. 将vowels替换为后面的字母

    vowels=['a','e','i','o','u']
    ciphertext=""
    for letter in message:
        if letter.isalpha():
            ciphertext=ciphertext+letter.upper()
        else:
            ciphertext=ciphertext+letter

    for letter in ciphertext:
        if letter in vowels:
            ciphertext=ciphertext.replace(letter,chr(ord(letter)+2))

    return ciphertext
