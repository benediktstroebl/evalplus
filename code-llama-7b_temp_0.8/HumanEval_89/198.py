
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
    a_dict = { 'a':'ijm', 'b':'nop', 'c':'qrs', 'd':'tuv', 'e':'wxy', 'f':'z01',
                'g':'234', 'h':'567', 'i':'890', 'j':'kab', 'k':'cde', 'l':'fgh',
                'm':'ijk', 'n':'lmn', 'o':'pqr', 'p':'stu', 'q':'vwx', 'r':'yz0',
                's':'123', 't':'456', 'u':'789', 'v':'0ab', 'w':'cde', 'x':'fgh',
                'y':'ijk', 'z':'lmn', '0':'o23', '1':'p45', '2':'q67', '3':'r89',
                '4':'st0', '5':'uv1', '6':'wx2', '7':'y34', '8':'z56', '9':'078'}

    return ''.join([a_dict.get(c, c) for c in s])
