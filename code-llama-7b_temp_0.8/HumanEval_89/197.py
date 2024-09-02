
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
    abet=list('abcdefghijklmnopqrstuvwxyz')
    abet.extend(abet[0:26])
    #abete=list('et')
    #abete=abete[0:26]
    #print(abete)
    abete=list(s)
    #abete.extend(abet[0:26])
    #print(abete)
    #print(abete.index('e'))
    #print(abete.index('t'))
    #abete.remove('t')
    #abete.remove('e')
    abete[abete.index('e')]=abete[abete.index('e')]+26
    abete[abete.index('t')]=abete[abete.index('t')]+26
    print(abete)
    #print(abete.index('e'))
    #print(abete.index('t'))
    for i in range(len(abete)):
        abete[i]=abet[abete[i]]
        #print(abete[i])
    print(abete)
    #print(abete.index('e'))
    #print(abete.index('t'))
    print(abete)
    #print(abete.index('e'))
    #print(abete.index('t'))
    #abete.remove(abete.index('e'))
    #abete.remove(abete.index('t'))
    return ''.join(abete)
