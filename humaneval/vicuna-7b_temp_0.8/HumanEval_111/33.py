
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
    s = test.split()
    num_items = len(s)
    num_of_letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_count = {}
    for i in range(num_items):
        count = 0
        for j in range(len(s)):
            if s[j] in letter_count:
                count += letter_count[s[j]]
        letter_count[s[i]] = count
    return letter_count
