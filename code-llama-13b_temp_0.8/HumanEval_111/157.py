
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
    test= test.split()
    hist= {}
    for l in test:
        if l in hist:
            hist[l]+=1
        else:
            hist[l]=1
    
    result=[]
    for i in hist.items():
        if i[1] == max(hist.values()):
            result.append(i[0])
    if len(result)==1:
        return {result[0]: hist[result[0]]}
    return dict(result)
