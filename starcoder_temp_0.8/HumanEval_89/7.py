
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
    x = len(s)
    i = 0
    r = ''
    while i < x:
        if s[i] =='':
            r = r +''
        elif s[i] == 'a' or s[i] == 'b' or s[i] == 'c' or s[i] == 'd' or s[i] == 'e' or s[i] == 'f' or s[i] == 'g' or s[i] == 'h' or s[i] == 'i' or s[i] == 'j' or s[i] == 'k' or s[i] == 'l' or s[i] =='m' or s[i] == 'n' or s[i] == 'o' or s[i] == 'p' or s[i] == 'q' or s[i] == 'r' or s[i] =='s' or s[i] == 't' or s[i] == 'u' or s[i] == 'v' or s[i] == 'w' or s[i] == 'x' or s[i] == 'y' or s[i] == 'z':
            r = r + chr(((ord(s[i])-ord('a')-2)*2)+ord('a'))
        elif s[i] == 'A' or s[i] == 'B' or s[i] == 'C' or s[i] == 'D' or s[i] == 'E' or s[i] == 'F' or s[i] == 'G' or s[i] == 'H' or s[i] == 'I' or s[i] == 'J' or s[i] == 'K' or s[i] == 'L' or s[i] == 'M' or s[i] == 'N' or s[i] == 'O' or s[i] == 'P' or s[i] == 'Q' or s[i] == 'R' or s[i] == 'S' or s[i] == 'T' or s[i] == 'U' or s[i] == 'V' or s[i] == 'W' or s[i]
