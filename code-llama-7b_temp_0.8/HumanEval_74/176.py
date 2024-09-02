
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    
    new_lst1=[]
    new_lst2=[]
    for i in lst1:
        new_lst1.append(len(i))
    for i in lst2:
        new_lst2.append(len(i))
    #print(new_lst1)
    #print(new_lst2)
    
    for i in range(len(new_lst1)):
        if new_lst1[i]<new_lst2[i]:
            new_lst1[i] = lst1[i]
            new_lst2[i] = ''
    for i in range(len(new_lst2)):
        if new_lst2[i]<new_lst1[i]:
            new_lst2[i] = lst2[i]
            new_lst1[i] = ''
    
    if new_lst1 == []:
        return new_lst2
    elif new_lst2 == []:
        return new_lst1
    else:
        return new_lst1







