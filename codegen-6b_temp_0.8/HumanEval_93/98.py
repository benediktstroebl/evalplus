
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
    
    # Strategy
    # 1. Find all vowels in message
    # 2. Replace them with the 2 characters that appear 2 places ahead of it
    # 3. Return result
    
    # Does all vowels need to be replaced? 
    # No, so we just return the message as is. 
    # This is essentially a default case. 
    # If there are vowels, we need to check if the letters after the vowels are within the range of letter
    if 'a' in message or 'e' in message or 'i' in message or 'o' in message or 'u' in message:
        
        # Find Vowels
        vowels = []
        for i in range(len(message)):
            if message[i] == 'a' or message[i] == 'e' or message[i] == 'i' or message[i] == 'o' or message[i] == 'u':
                vowels.append(i)
                
        # Replace Vowels
        for i in vowels:
            # Check for letter that is 2 places ahead
            temp = message[i-2:i+1]
            if temp in 'aeiou':
                message = message[0:i-2] + temp + message[i+1:]
                message = message[:i+1] + temp + message[i-1:]
    
    return message 
    
    