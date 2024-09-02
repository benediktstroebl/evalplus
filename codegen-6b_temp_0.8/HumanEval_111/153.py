
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
    # Hint: use a return statement and a dictionary (or more accurately, a hash table) to count
    # the number of each letter. For example if the input is 'a b c', the dictionary should be {'a': 1, 'b': 1, 'c': 1}.
    # Make sure to use the dictionary only for distinct letters. Use a more efficient and iterative approach if your
    # dictionary is big.

    # if test == '': return {}
    dic = {}
    for c in test:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    max_freq = max(dic.values())

    return {k: v for k,v in dic.items() if v == max_freq}


