
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
    END_TO_CODE = {'a':'0',
                  'b':'1',
                  'c':'2',
                  'd':'3',
                  'e':'4',
                  'f':'5',
                  'g':'6',
                  'h':'7',
                  'i':'8',
                  'j':'9',
                  'k':'a',
                  'l':'b',
                  'm':'c',
                  'n':'d',
                  'o':'e',
                  'p':'f',
                  'q':'g',
                  'r':'h',
                  's':'i',
                  't':'j',
                  'u':'k',
                  'v':'l',
                  'w':'m',
                  'x':'n',
                  'y':'o',
                  'z':'p',
                  ' ':' ',
                  'O':'0',
                  'a':'1',
                  'i':'2',
                  'e':'3',
                  'u':'4',
                  'o':'5',
                  'y':'6',
                  'O':'0'
                  }
    vowels = ['a','e','i','o','u','y']
    
    def encode_helper(string, result):
        if string == '':
            return result
        if string[0].isalpha():
            code_word = END_TO_CODE[string[0].lower()]
            result += code_word
            vowel_count = string.count(string[0])
            for i in range(1, vowel_count):
                string = string[1:]
                result += code_word
            return encode_helper(string[1:], result)
        else:
            return encode_helper(string[1:], result + ' ')
    
    return encode_helper(message, '')
