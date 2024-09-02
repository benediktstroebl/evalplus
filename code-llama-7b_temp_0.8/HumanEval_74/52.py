
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

    lst3 = []
    if lst1 == [] and lst2 == []:
        return []
    elif len(lst1) > len(lst2):
        for el in lst2:
            total = 0
            for i in el:
                total += ord(i)
            lst3.append(total)
        lst4 = []
        for i in lst3:
            for el in lst2:
                if i == sum(ord(x) for x in el):
                    lst4.append(el)
        return lst4
    else:
        for el in lst1:
            total = 0
            for i in el:
                total += ord(i)
            lst3.append(total)
        lst4 = []
        for i in lst3:
            for el in lst1:
                if i == sum(ord(x) for x in el):
                    lst4.append(el)
        return lst4


