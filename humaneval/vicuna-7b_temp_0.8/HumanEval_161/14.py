
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    # use a dictionary to map each letter to its uppercase or lowercase form
    map_dict = {ord(letter): chr(ord(letter) ^ 0x40).encode('utf8') for letter in s}
    
    # use a list to keep track of the current position
    current = []
    
    # use a generator function to iterate through the string
    for letter in s:
        if ord(letter) > 128:
            current.append(ord(letter))
        else:
            if letter in map_dict:
                yield map_dict[letter]
            else:
                if current[-1] != ord(letter):
                    yield current.pop(0)
                current.append(ord(letter))
    
    # return the reversed string
    return ''.join(reversed(current))
