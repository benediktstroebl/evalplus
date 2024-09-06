
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
    # We'll use a dictionary to store the new letters.
    # The keys are the old letters and the values are the new ones.
    code_book = {}

    # This will hold the final answer.
    encoded_message = ''

    # Loop through the string, creating a dictionary of the
    # letters and their codes.
    for character in message:

        # If this letter is in the code_book, we'll use its code,
        # otherwise we'll use the letter itself.
        encoded_message += code_book.get(character, character)

        # If this character is a vowel, we'll need to add a code
        # to the code_book.
        if character in ['a', 'e', 'i', 'o', 'u']:
            code_book[character] = message[(message.index(character) + 2) % len(message)]

    # return the encoded message.
    return encoded_message
