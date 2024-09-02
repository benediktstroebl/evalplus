
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
    #starting to use split
    #the list will be a list of letters that will be encrypted
    result = list(s)

    #first we should split it to a list
    #result = list(s)
    #print(result)
    #letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #print(letters)
    #now we should find the index of the letters in the string
    #for i in range(0,len(result)):

    for i in result:
        #print(i)
        #print(result[i])
        if i=='a':
            #print('a')
            result[i]='c'
        if i=='b':
            #print('b')
            result[i]='d'
        if i=='c':
            #print('c')
            result[i]
