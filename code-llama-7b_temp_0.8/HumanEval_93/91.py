
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
    
    # Step 1
    # Write a function that takes in a string and returns it with all the vowels removed.
    def remove_vowels(message):
        new_message = ''
        for char in message:
            if char.lower() not in 'aeiou':
                new_message += char
        return new_message
    
    # Step 2
    # Write a function that takes in a string and returns it with all the letters swapped with their corresponding letter 2 places behind.
    def shift_letters(message):
        new_message = ''
        for char in message:
            if char.isalpha():
                pos = ord(char)
                if char.islower():
                    new_pos = (pos + 2) % 26 + ord('a')
                else:
                    new_pos = (pos + 2) % 26 + ord('A')
                new_message += chr(new_pos)
            else:
                new_message += char
        return new_message
    
    # Step 3
    # Write a function that takes in a string and returns it with all the letters in uppercase.
    def to_upper(message):
        new_message = ''
        for char in message:
            if char.isalpha():
                new_message += char.upper()
            else:
                new_message += char
        return new_message
    
    # Step 4
    # Write a function that takes in a string and returns it with all the letters in lowercase.
    def to_lower(message):
        new_message = ''
        for char in message:
            if char.isalpha():
                new_message += char.lower()
            else:
                new_message += char
        return new_message
    
    return to_upper(shift_letters(remove_vowels(to_lower(message))))
    
