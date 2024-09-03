def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead, and only 
    allows letters.

    Args:
    message (str string)

    Returns:
    string with encoded message
    """
    encoding = []
    for c in message:
        if c.isalpha():
            encoding.append(c)
        else:
            encoding.append(c[2])
    return ''.join(encoding)