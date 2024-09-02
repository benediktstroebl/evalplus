
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
    return s.translate(str.maketrans({
        'a': 'Z',
        'b': 'Y',
        'c': 'X',
        'd': 'W',
        'e': 'U',
        'f': 'T',
        'g': 'R',
        'h': 'Q',
        'i': 'P',
        'j': 'O',
        'k': 'N',
        'l': 'M',
        'm': 'L',
        'n': 'K',
        'o': 'J',
        'p': 'I',
        'q': 'H',
        'r': 'G',
        's': 'F',
        't': 'E',
        'u': 'S',
        'v': 'B',
        'w': 'D',
        'x': 'C',
        'y': 'B',
        'z': 'A',
        'A': 'Z',
        'B': 'Y',
        'C': 'X',
        'D': 'W',
        'E': 'U',
        'F': 'T',
        'G': 'R',
        'H': 'Q',
        'I': 'P',
        'J': 'O',
        'K': 'N',
        'L': 'M',
        'M': 'L',
        'N': 'K',
        'O': 'J',
        'P': 'I',
        'Q': 'H',
        'R': 'G',
        'S': 'F',
        'T': 'E',
        'U': 'S',
        'V': 'B',
        'W': 'D',
        'X': 'C',
        'Y': 'B',
        'Z': 'A'
    }))

