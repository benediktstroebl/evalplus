
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a dictionary to check if the length of the string is a prime number
    prime_numbers = {
        2: True,
        3: True,
        5: True,
        7: True,
        11: True,
        13: True,
        17: True,
        19: True,
        23: True,
        29: True,
        31: True,
        37: True,
        41: True,
        43: True,
        47: True,
        53: True,
        59: True,
        61: True,
        67: True,
        71: True,
        73: True,
        79: True,
        83: True,
        89: True,
        97: True,
        101: True,
        103: True,
        107: True,
        109: True,
        113: True,
        127: True,
        131: True,
        137: True,
        149: True,
        151: True,
        157: True,
        163: True,
        167: True,
        173: True,
        179: True,
        181: True,
        193: True,
        197: True,
        199: True,
        211: True,
        223: True,
        229: True,
        233: True,
        239: True,
        241: True,
        247: True,
        251: True,
        257: True,
        263: True,
        269: True,
        271: True,
        277: True,
        281: True,
        283: True,
        293: True,
        307: True,
        311: True,
        313: True,
        317: True,
        331
