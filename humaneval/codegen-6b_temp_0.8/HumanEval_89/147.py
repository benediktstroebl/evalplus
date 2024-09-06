
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
    
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = """
                  ^
                ^   ^
              ^       ^
            ^           ^
          ^                       ^
        ^                                  ^
      ^                                   ^
    ^                                 ^   ^
  ^                                  ^^^
 ^                                   ^
      ^   ^   ^  ^      ^
      ^     ^^
      ^                 ^
       ^
        ^    ^
        ^
         ^
          ^
         ^
        ^
        ^
    """.strip().split('\n')
    for i, line in enumerate(alphabet2):
        alphabet2[i] = line.replace(' ','')

    def rot(text, shift):
        return ''.join([alphabet2[(alphabet2.index(letter)+shift)%26] for letter in text])

    return rot(s,26-len(s))
