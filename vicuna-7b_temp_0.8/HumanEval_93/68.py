
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

    # Define a dictionary to map vowels to their positions in the alphabet
    vowels = "aeiouAEIOU"
    mapping = {vowels[i]: i+1 for i in range(len(vowels))}

    # Define a function to reverse a string
    def reverse_string(s):
        return s[::-1]

    # Define a function to convert a string to lowercase
    def lowercase(s):
        return s.lower()

    def encode_word(word):
        # Reverse the string
        word = reverse_string(word)
        
        # Replace all vowels with their mapped values
        word = word.translate(lambda x: mapping[x] if x in mapping else x for x in word)
        
        return word

    def encode_message(message):
        # Convert the message to lowercase
        message = lowercase(message)

        # Replace all vowels with their mapped values
        message = message.translate(lambda x: mapping[x] if x in mapping else x for x in message)
        
        # Replace all vowels with their mapped values
        message = message.translate(lambda x: mapping[x] if x in mapping else x for x in message)

        return message

    return encode_message(message)
