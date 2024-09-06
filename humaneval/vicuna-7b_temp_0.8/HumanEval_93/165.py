
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
    #convert message to lowercase
    message = message.lower()
    #split message into characters
    message = message.split()
    #initialize an empty list to store encoded characters
    encoded_characters = []
    #iterate through each character in the message
    for char in message:
        #check if char is a vowel
        if char in 'aeiou':
            #determine index of next vowel in english alphabet
            index = [0, 1, 3, 6, 7, 8, 9, 12, 13, 15, 16, 17, 19, 20, 21, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 77, 78, 79, 80, 81, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 97, 98, 99, 101, 102, 103, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
