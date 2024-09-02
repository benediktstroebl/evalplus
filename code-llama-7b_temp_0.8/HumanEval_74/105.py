
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
    final_lst = []

    for i in lst1:
        total = 0
        for letter in i:
            total += ord(letter)
        final_lst.append(total)

    for i in lst2:
        total = 0
        for letter in i:
            total += ord(letter)
        final_lst.append(total)

    final_lst = list(set(final_lst))
    final_lst.sort()
    print(final_lst)
    new_lst = []
    for i in final_lst:
        for j in lst1:
            total = 0
            for letter in j:
                total += ord(letter)
            if i == total:
                new_lst.append(j)
                break
    print(new_lst)
    new_lst = []
    for i in final_lst:
        for j in lst2:
            total = 0
            for letter in j:
                total += ord(letter)
            if i == total:
                new_lst.append(j)
                break
    print(new_lst)

    if len(new_lst) == len(lst1):
        return lst1
    elif len(new_lst) == len(lst2):
        return lst2

