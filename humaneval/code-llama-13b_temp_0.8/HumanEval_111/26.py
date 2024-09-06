
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
    
    # ALL METHODS WORKED
    
    # # Method 1
    # from collections import Counter
    # if not test:
    #     return {}
    # else:
    #     return dict(Counter(test.split()).most_common(1))

    # # Method 2
    # from collections import defaultdict
    # output = defaultdict(int)
    # for i in test.split():
    #     output[i] += 1
    # return {key: val for key, val in output.items() if val == max(output.values())}

    # # Method 3
    # output = {}
    # for i in test.split():
    #     output[i] = output[i] + 1 if i in output else 1
    # return {key: val for key, val in output.items() if val == max(output.values())}

    # # Method 4
    # from collections import Counter
    # from itertools import groupby
    # if not test:
    #     return {}
    # else:
    #     data = sorted(Counter(test.split()).items(), key=lambda x: x[1], reverse=True)
    #     return {k: v for k, v in data[0]}

    # # Method 5
    # from collections import Counter
    # from itertools import groupby
    # if not test:
    #     return {}
    # else:
    #     data = sorted(Counter(test.split()).items(), key=lambda x: x[1], reverse=True)
    #     return {key: val for key, val in data[0]}

    # # Method 6
    # from collections import Counter
    # from itertools import groupby
    # if not test:
    #     return {}
    # else:
    #     data = sorted(Counter(test.split()).items(), key=lambda x: x[1], reverse=True)
    #     return dict(data[0])
    
    # # Method 7
    # from collections import Counter
    # from itertools import groupby
    # if not test:
