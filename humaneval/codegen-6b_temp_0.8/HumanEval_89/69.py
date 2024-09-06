
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    s = s.lower()
    shift = ord('a')-ord('a')
    combos = {chr(ord('a')+i) : chr(ord('a')+i+shift*2) for i in range(0,26)} 
    combos['-'] = '-'
    combos[' '] = ' '
    combos_inv = {chr(ord('a')+i) : chr(ord('a')+i-2*shift) for i in range(0,26)}
    combos_inv['-'] = '-'
    combos_inv[' '] = ' '
    return "".join(combos[c] if c in combos else c for c in s)
