
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

    #first split the string into letters, put them in a list, and then count the number of times they appear
    #put the counts in a dictionary
    letters=test.split()
    count=dict.fromkeys(letters, 0)
    for x in letters:
        count[x]+=1
    #now delete the key value pairs from the dictionary with a count of 1
    for k, v in count.items():
        if v == 1:
            del count[k]
    return count

    #now put the keys and counts back in the list
    a=[]
    for k, v in count.items():
        a.append([k, v])
    #sort it alphabetically
    a.sort()
    #change it to a set
    a=set(a)
    #put it back in a dictionary
    new=dict(a)
    return new



