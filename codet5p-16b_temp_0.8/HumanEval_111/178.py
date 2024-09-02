
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

    s=test.split(' ')
    letter_count={}
    for i in s:
        if i in letter_count:
            letter_count[i]+=1
        else:
            letter_count[i]=1

    maxi=max(letter_count.values())
    result={}
    for i in letter_count:
        if letter_count[i]==maxi:
            result[i]=maxi
    return result

