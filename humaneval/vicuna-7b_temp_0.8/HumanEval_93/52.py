
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
    message = message.upper()  # 将字符串转换成大写字符串
    # 对字符串进行归并化操作
    message = "".join(map(str, message))
    # 尝试使用字典来替换字符
    message = message.translate(str.maketrans("", "", "aeiou"))
    # 对字符串进行反转操作
    message = message.translate(str.maketrans("", "", "NmeIorU"))
    return message