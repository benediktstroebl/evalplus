
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
    # Remove spaces and special characters.
    s = re.sub('[^a-zA-Z]+', '', s)
    # If no letters, return a blank string.
    if s == '':
        return ''
    # Create the dictionary of char (letter) to num (index)
    dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    # Rotate letters using dictionary above to create the result string.
    result = ''
    if len(s) > 1:
        for i in range(0, len(s)):
            if i < len(s):
                result += chr(dict[s[i]] + ((dict[s[i-1]] + 2) * 2) + 2)
            else:
                result += chr(dict[s[i]] + ((dict[s[i-1]] + 2) * 2) + 2)
    else:
        result += s[0]
    return result 
