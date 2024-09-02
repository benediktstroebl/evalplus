

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    s = ' ' * (n - 1) + str(n)
    while True:
        c = input('Enter next number: ')
        if c.isdigit():
            n = int(c)
            s = s[:-1] + str(n) + s[1:]
        else:
            print('Invalid input')
            break
    
    return s
