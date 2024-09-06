
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

    
    count_list = []

    if len(lst1) == len(lst2):
        count_list.append(lst1)
        return count_list

    elif len(lst1) < len(lst2):
        for i in range(len(lst2)):
            count = 0
            for j in range(len(lst1)):
                if lst1[j] == lst2[i]:
                    count += 1
            if len(lst1) == count:
                count_list.append(lst2[i])
        return count_list

    elif len(lst1) > len(lst2):
        for i in range(len(lst1)):
            count = 0
            for j in range(len(lst2)):
                if lst1[i] == lst2[j]:
                    count += 1
            if len(lst2) == count:
                count_list.append(lst1[i])
        return count_list
