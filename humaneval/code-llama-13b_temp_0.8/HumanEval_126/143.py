
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    #create a list that holds only unique numbers
    #the list.index() function returns the first instance of the number,
    #so if the list has any duplicates, they will be found by index()
    if len(lst) == 1:
        return True
    elif len(lst) == 2:
        return lst[0] < lst[1]
    else:
        uniq = []
        for num in lst:
            if num not in uniq:
                uniq.append(num)
            else:
                return False
    for i in range(len(uniq)):
        if i == 0:
            if uniq[i] > uniq[i+1]:
                return False
        elif i == len(uniq) - 1:
            if uniq[i] < uniq[i-1]:
                return False
        else:
            if uniq[i] > uniq[i+1]:
                return False
            elif uniq[i] < uniq[i-1]:
                return False
    return True

