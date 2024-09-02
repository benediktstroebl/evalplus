
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
    max_value = -1
    for i in range(len(lst)):
        if (lst[i] > 0):
            current_value = lst[i]
            current_frequency = 1
            for j in range(i+1, len(lst)):
                if (lst[j] == current_value):
                    current_frequency += 1
                else:
                    break

            if (current_frequency >= current_value):
                if (current_frequency > max_value):
                    max_value = current_frequency

    return max_value
