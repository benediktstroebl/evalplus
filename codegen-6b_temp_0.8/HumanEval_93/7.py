
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
    def swap_char(c):
        swap_dict = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9', 'k':'a', 'l':'b', 'm':'c', 'n':'d', 'o':'e', 'p':'f', 'q':'g', 'r':'h', 's':'i', 't':'j', 'u':'k', 'v':'l', 'w':'m', 'x':'n', 'y':'o', 'z':'p'}
        a = swap_dict[c]
        return a
    
    def replace_letter(m):
        r_dict = {'a':'1', 'b':'!', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9', 'k':'0', 'l':'1', 'm':'2', 'n':'3', 'o':'4', 'p':'5', 'q':'6', 'r':'7', 's':'8', 't':'9', 'u':'@', 'v':'A', 'w':'B', 'x':'C', 'y':'D', 'z':'E'}
        b = r_dict[m]
        return b
    
    def encode_message_1(m):
        result = ""
        for c in m:
            result += replace_letter(c)
        return result
    
    def encode_message_2(m):
        result = ""
        for c in m:
            result += swap_char(c)
        return result
    
    return encode_message_1(message)
    # return encode_message_2(message)
