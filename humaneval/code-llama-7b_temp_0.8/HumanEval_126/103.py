
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
    #create a list of the unique values
    unique_values = []
    for i in lst:
        if i not in unique_values:
            unique_values.append(i)

    #create a list of the values with the number of unique values
    values_to_count = []
    for i in range(len(unique_values)):
        for j in lst:
            if j == unique_values[i]:
                values_to_count.append(j)

    #check to make sure the number of values equals the number of times the value appears
    for i in values_to_count:
        if values_to_count.count(i) != unique_values.count(i):
            return False
    return True





