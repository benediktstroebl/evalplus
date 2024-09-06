
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
    #...
    #break this down
    #letter = string.lower()
    #encrypted = []
    #for letter in string:
     #   encrypted.append(letter)
     #   encrypted = string.lower()
     #   for letter in string.lower():
     #       if letter >= 'a' and letter <= 'z':
     #           letter = ord(letter) - ord('a') - 2
     #           letter = chr(letter + ord('a'))
     #           encrypted.append(letter)
     #           #print(string.lower())

     #return "".join(encrypted)
    #...
    s = s.lower()
    for i in range(len(s)):
        if s[i] >= "a" and s[i] <= "z":
            s[i] = ord(s[i]) - ord('a') - 2
            s[i] = chr(s[i] + ord('a'))
    return "".join(s)
