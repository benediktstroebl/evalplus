
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
    alphabet=[]
    my_dict={}
    for x in test:
        alphabet.append(x)

    for x in alphabet:
        if alphabet.count(x)==1:
            my_dict[x]=1
        elif alphabet.count(x)>=1:
            my_dict[x]=alphabet.count(x)
    return my_dict
