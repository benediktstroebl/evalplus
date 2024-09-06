
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
    list1=test.split(" ")
    list2=[]
    for i in list1:
        list2.append(i)
    list3=set(list2)
    list4=[]
    for i in list3:
        list5=list2.count(i)
        list4.append(list5)
    d1={}
    for i,j in zip(list3,list4):
        d1[i]=j
    return d1
