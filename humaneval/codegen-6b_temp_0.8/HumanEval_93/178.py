
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
    
    #pass
    
    vowels = ['a','e','i','o','u']
    
    translate = [('a','e','i','o','u'),('A','E','I','O','U'),
                 ('b','g','d','t','k'),('B','G','D','T','K'),
                 ('c','h','f','s','v'),('C','H','F','S','V'),
                 ('d','l','n','m','w'),('D','L','N','M','W'),
                 ('e','n','r','s','j'),('E','N','R','S','J'),
                 ('f','q','v','n','x'),('F','Q','V','N','X'),
                 ('g','r','u','v','n'),('G','R','U','V','N'),
                 ('h','t','s','u','d'),('H','T','S','U','D'),
                 ('i','y','u','f','v'),('I','Y','U','F','V'),
                 ('j','k','q','w','x'),('J','K','Q','W','X'),
                 ('k','w','h','k','l'),('K','W','H','K','L'),
                 ('l','l','x','s','p'),('L','X','S','P','S'),
                 ('m','n','v','c','b'),('M','N','V','C','B'),
                 ('n','n','m','p','q'),('N','P','Q','N','Q'),
                 ('o','r','s','p','g'),('O','R','S','P','G'),
                 ('p','o','y','t','g'),('P','Y','T','G','G'),
                 ('q','u','a','t','l'),('Q','U','A','T','L'),
                 ('r','a','h','w','n'),('R','A','H','W','N'),
                 ('s','i','d','f','c'),('S','I','D','F','C'),
                 ('t','o','v','b','l'),('T','O','V','B','L'),
                 