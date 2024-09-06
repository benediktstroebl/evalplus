
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
    #split the input
    list1= test.split(' ')
    #define dictionary
    dict1 = {}
    #define input to be empty
    dict1={}
    #make list1 empty
    list1=[]
    #create empty set
    set1 = set()
    
    #if len(list1)==0:
      #return dict1
    for i in list1:
        dict1[i]=list1.count(i)
        #if list1.count(i) == max(dict1.values()):
            #set1.add(i)
            #return dict1
    #if list1.count(i) >= max(dict1.values()):
        #return dict1
    #for i in dict1:
        #if dict1[i] == max(dict1.values()):
            #set1.add(i)
    #return set1
    for i in dict1:
        if dict1[i] == max(dict1.values()):
            set1.add(i)
    return set1
