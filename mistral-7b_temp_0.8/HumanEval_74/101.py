
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
    count1=0
    count2=0
    newlst1=[]
    newlst2=[]
    for i in lst1:
        for j in i:
            count1+=1
        newlst1.append(count1)
        count1=0
    for i in lst2:
        for j in i:
            count2+=1
        newlst2.append(count2)
        count2=0
    if len(newlst1) > len(newlst2):
        return lst2
    if len(newlst1) < len(newlst2):
        return lst1
    if len(newlst1) == len(newlst2):
        return lst1
