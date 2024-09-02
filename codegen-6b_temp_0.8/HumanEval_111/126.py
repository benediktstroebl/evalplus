
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
    # Alternative: use Counter from collections module
    # import collections
    # return collections.Counter(test)
    # Alternatively, use defaultdict from collections module:
    # from collections import defaultdict
    # hist = defaultdict(int)
    # for letter in test:
    #     hist[letter] += 1
    # return hist
    # Alternatively, use dictionary comprehension:
    # hist = {letter: 1 for letter in test}
    # return hist
    # Another way: use maketrans from string module:
    # transtab = str.maketrans('abc', 'cba')
    # return {test[i]: test.count(test[i]) for i in range(len(test))}.translate(transtab)
    # Alternatively, use itertools.groupby instead of counting
    # hist = {}
    # for i, letter in enumerate(test):
    #     if i == 0:
    #         hist[letter] = 1
    #     else:
    #         if letter in hist:
    #             hist[letter] += 1
    #         else:
    #             hist[letter] = 1
    # return hist
    
    # Alternatively, use collections.Counter (defaultdict from collections module)
    # from collections import Counter
    # hist = Counter(test)
    # return hist 

    # Alternativly, use Counter in memory
    # hist = Counter(test)
    # hist = {}
    # for letter in test:
    #     if letter in hist:
    #         hist[letter] += 1
    #     else:
    #         hist[letter] = 1
    # return hist
    
    return {}

