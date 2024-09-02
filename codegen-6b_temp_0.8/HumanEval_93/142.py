
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
    remap = defaultdict(lambda: '', {'A': '', 'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '', 'M': '', 'N': '', 'O': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'T': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Y': '', 'Z': ''})
    # get list of all english vowels
    vowels = re.findall('[aeiou]', message)
    for vowel in vowels:
        # find indeces of each vowel
        first = message.find(vowel)
        second = message.find(vowel, first+1)
        # swap vowels
        remap[message[first]] = message[second]
        remap[message[second]] = message[first]
    # modify message, removing vowels and replacing with transformed vowels
    return re.sub('[aeiouAEIOU]', '', message).translate(remap)
