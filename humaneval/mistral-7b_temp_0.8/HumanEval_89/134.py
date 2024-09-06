
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
    word = ""
    if len(s) > 0:
        word = s[0]
        for i in range(1, len(s)):
            word += s[i]
    else:
        word = " "
    print("word is " + word)
    for i in range(0, len(word)):
        # print(word[i])
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            # print(word[i])
            new_val = ord(word[i]) + 2*2
            # print("new val is " + str(new_val))
            word = word[:i] + chr(new_val) + word[i+1:]
            print(word)
        if ord(word[i]) >= 65 and ord(word[i]) <= 90:
            new_val = ord(word[i]) + 2*2
            word = word[:i] + chr(new_val) + word[i+1:]
            print(word)
    
