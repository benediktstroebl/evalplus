
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
    if test == "":
        return {}
    else:
        test2 = test.split()
        if len(test2) == 1:
            return {test2[0] : 1}
        else:
            dico = {}
            for i in range(0,len(test2)):
                if test2[i] not in dico.keys():
                    dico[test2[i]] = 1
                else:
                    dico[test2[i]] += 1
                
            maxi = max(dico.values())
            result = {}
            for key, value in dico.items():
                if value == maxi:
                    result[key] = value
            return result
