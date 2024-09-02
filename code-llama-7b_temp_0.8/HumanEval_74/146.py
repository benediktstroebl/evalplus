
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

    if not lst1 or not lst2:
        return []
    
    list1 = list()
    for element in lst1:
        for sub_element in element:
            list1.append(sub_element)
    
    list2 = list()
    for element in lst2:
        for sub_element in element:
            list2.append(sub_element)

    list1_string = "".join(list1)
    list2_string = "".join(list2)

    if len(list1_string) <= len(list2_string):
        return lst1
    else:
        return lst2

