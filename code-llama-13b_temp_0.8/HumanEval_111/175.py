
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
    # your code here

    # if test == "":
    #     return {}
    # else:
    #     values = test.split(" ")
    #     values = list(filter(None, values))
    #     results = {}
    #     for i in values:
    #         if i in results.keys():
    #             results[i] += 1
    #         else:
    #             results[i] = 1
    #     return results


    if test == "":
        return {}
    else:
        values = test.split(" ")
        values = list(filter(None, values))
        results = {}
        for i in values:
            if i in results.keys():
                results[i] += 1
            else:
                results[i] = 1
        return results

