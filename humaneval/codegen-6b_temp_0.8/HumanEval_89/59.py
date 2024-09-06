
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
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # list of tuples for each letter in alphabet
    # each tuple consists of (index, alphabet)
    tuples = list(enumerate(arr))

    # add a third tuple to array, which will be the space char
    tuples.append(len(tuples))

    space_char = tuples[-1][1]

    # apply string rotation
    for i in range(len(tuples)):
        if tuples[i][1].lower() == s.lower():
            tuples[i] = (i, tuples[i][1].lower())

    index = tuples.index(-1)
    first = tuples[index][0]

    # rotate the letters by 2x
    second = (first + 2) % len(tuples)

    # convert tuple values to string
    arr_string = [str(i) for i in tuples]

    # build encrypted string
    encrypted = "".join(arr_string[first:second])
    encrypted = encrypted + space_char

    return encrypted

