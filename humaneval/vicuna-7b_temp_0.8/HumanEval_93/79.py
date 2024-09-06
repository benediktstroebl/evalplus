
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
    # Split the message into a list of letters
    words = message.split()
    # Convert the words to lowercase
    words = [word.lower() for word in words]
    # Reverse the order of the letters in each word
    words = [word[::-1] for word in words]
    # Initialize a dictionary to store the positions of each vowel
    vowel_pos = {}
    for i, char in enumerate(words):
        if char in "aeiou":
            vowel_pos[char] = i + 1
    # Loop through the words
    for word in words:
        # Loop through the characters in the word
        for i, char in enumerate(word):
            if char in "aeiou":
                # If the current character is a vowel, replace it
                # with the character that appears 2 places ahead of 
                # that vowel in the english alphabet
                if vowel_pos[char] in vowel_pos:
                    word[i] = vowel_pos[vowel_pos[char]]
                    del vowel_pos[vowel_pos[char]]
                else:
                    word[i] = char
        # If the current character is a vowel, replace it
        # with the character that appears 2 places ahead of 
        # that vowel in the english alphabet
        if word[i] in "aeiou":
            word[i] = vowel_pos[word[i]]
    # Initialize a new list to store the encoded message
    encoded_message = []
    # Loop through the words
    for word in words:
        # If the word is empty, add a space to the encoded message
        if not word:
            encoded_message.append(" ")
        # If the word is not empty, add the word with the vowels 
        # replaced and in uppercase to the encoded message
        else:
            encoded_message.append(word.upper())
    # Return the encoded message
    return "".join(encoded_message)
