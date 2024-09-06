
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    counter = {}
    for elem in lst:
        if counter.get(elem, 0) == 0:
            counter[elem] = 1
        else:
            counter[elem] += 1
    print(counter)
    min_value = min(counter, key=counter.get)
    print(min_value)
    min_value_counter = counter[min_value]
    print(min_value_counter)
    for key in counter:
        if counter.get(key) >= min_value_counter and key > min_value:
            return key
    return -1

