
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
    if test == "":
        return {}
    else:
        ans = {}
        for x in test.split():
            if x in ans:
                ans[x] += 1
            else:
                ans[x] = 1
        ans = {k: v for k, v in ans.items() if v == max(ans.values())}
        return ans
