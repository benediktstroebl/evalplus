
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
    dic={}
    lista=[]
    for i in test:
        if i in dic:
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    for i in test:
        if i not in lista:
            lista.append(i)
    ans={}
    for i in lista:
        if dic[i]==max(dic.values()):
            ans[i]=dic[i]
    return ans
        

