
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
    total_lst1=[]
    for i in lst1:
        sum=0
        for j in i:
            sum+=len(j)
        total_lst1.append(sum)
    total_lst2=[]
    for i in lst2:
        sum=0
        for j in i:
            sum+=len(j)
        total_lst2.append(sum)
    total_lst1.sort()
    total_lst2.sort()
    if total_lst1[0] == total_lst2[0]:
        return lst1
    elif total_lst1[0] < total_lst2[0]:
        return lst1
    else:
        return lst2
