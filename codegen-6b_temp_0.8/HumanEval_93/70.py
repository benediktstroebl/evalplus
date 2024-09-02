
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
    
    # XOO
    
    # This solution was inspired by: 
    # http://stackoverflow.com/questions/12094516/string-translating-without-knowing-the-codepage
    
    # Create a table of hash keys
    # for each letter in the message
    # create a hash key
    # remove all non-letters
    # replace with character two ahead of the letter
    # add non-letters back to string
    
    # For example:
    # 'a' = 'alpha'
    # 'b' = 'bravo'
    # 'C' = 'charlie'
    # 'e' = 'echo'
    # 'f' = 'foxtrot'
    # 'h' = 'hotel'
    # 'i' = 'india'
    # 'l' = 'lucas'
    # 'm' = 'mike'
    # 'o' = 'alpha'
    # 'p' = 'papa'
    # 'r' = 'randy'
    # 's' = 'sierra'
    # 't' = 'tango'
    # 'w' = 'whiskey'
    # 'x' = 'xray'
    # 'z' = 'zulu'
    #
    # This is the translation table:
    # { 'a' : 'alpha',
    #   'c' : 'charlie',
    #   'e' : 'echo',
    #   'f' : 'foxtrot',
    #   'h' : 'hotel',
    #   'i' : 'india',
    #   'l' : 'lucas',
    #   'm' : 'mike',
    #   'o' : 'alpha',
    #   'p' : 'papa',
    #   'r' : 'randy',
    #   's' : 'sierra',
    #   't' : 'tango',
    #   'w' : 'whiskey',
    #   'x' : 'xray',
    #   'z' : 'zulu' }
    #