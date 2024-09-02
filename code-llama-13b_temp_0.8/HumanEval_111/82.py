
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
    
    # Empty input
    if test == "":
        return {}
    
    # Input is one word
    elif test.count(" ") == 0:
        return {test: 1}
    
    else:
        test_dic = {}
        for i in test.split(" "):
            if i not in test_dic:
                test_dic[i] = 1
            else:
                test_dic[i] += 1

        max_value = max(test_dic.values())
        result = {}
        for i in test_dic.keys():
            if test_dic[i] == max_value:
                result[i] = test_dic[i]
                
        return result
            
