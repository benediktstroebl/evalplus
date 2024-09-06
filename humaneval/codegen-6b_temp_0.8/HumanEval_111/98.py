
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # test = 'a b c'
    # test = 'a b b a'
    # test = 'a b c a b'
    # test = ''
    # test = 'b b b b a'
    # test = 'a a a a a'
    # test = 'b a b a a'
    # test = 'a b . c'
    # test = 'b b b b a'
    # test = 'a a . b b'
    # test = 'b . b . b . b'
    # test = 'a . b . c'
    # test = 'b . b . a'
    # test = '. b b b',
    # test = 'a b .'
    # test = 'a . c'
    # test = 'a a'
    # test = 'a'
    # test = 'b'
    # test = 'c'
    # test = 'a c a c'
    # test = 'a b c a c a b'
    # test = 'b'
    # test = 'b b b'
    # test = 'b b'
    # test = 'a'
    # test = 'a a'
    # test = 'a a a a a'
    # test = 'a a a'
    # test = 'a'
    # test = 'a a a a'
    # test = 'a a'
    # test = 'a a a a b'
    # test = 'a a'

    # test = 'aaaaaa'
    # test = 'aabbbaa'
    # test = 'aabbbbaa'
    # test = 'aabbaa'
    # test = 'baaabab'
    # test = 'baaabaaaaabaaaaabaaaaa'
    # test = 'bbaaababaabababababbbaa'
    # test = 'bbaababababababaababba'
    # test = 'aabaabaaabbbaaaaaabbaaabaaaabbbaabc'
    # test = 'aaaaabbbbaa'
    # test = 'aaaaabbbbaa'
    # test = 'aaaaabbbbaa'