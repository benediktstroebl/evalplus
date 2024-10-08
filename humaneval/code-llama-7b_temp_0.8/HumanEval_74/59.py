
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
    list1_total = 0
    list2_total = 0
    lst1_small = []
    lst2_small = []
    for i in lst1:
        list1_total += len(i)
    for i in lst2:
        list2_total += len(i)
    if list1_total > list2_total:
        return lst2
    if list1_total < list2_total:
        return lst1
    if list1_total == list2_total:
        return lst1
    
    

