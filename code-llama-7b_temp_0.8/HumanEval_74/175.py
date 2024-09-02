
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

    #Clean both lists
    lst1_clean = [x.lower() for x in lst1]
    lst2_clean = [x.lower() for x in lst2]

    #Create a dictionary with all the chars and the number of times they occur
    dic1 = {}
    for x in lst1_clean:
        for char in x:
            if char in dic1:
                dic1[char] += 1
            else:
                dic1[char] = 1

    dic2 = {}
    for x in lst2_clean:
        for char in x:
            if char in dic2:
                dic2[char] += 1
            else:
                dic2[char] = 1

    total1 = sum(dic1.values())
    total2 = sum(dic2.values())

    if total1 == total2:
        return lst1_clean

    if total1 > total2:
        return lst2_clean
    
    return lst1_clean

