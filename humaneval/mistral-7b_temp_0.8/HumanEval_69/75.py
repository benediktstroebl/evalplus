
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
    temp_list = list(set(lst))
    if len(temp_list) == 1:
        return -1
    else:
        max_freq = 0
        max_val = -1
        for i in range(len(temp_list)):
            if temp_list[i] > 0:
                if temp_list[i] > max_val and lst.count(temp_list[i]) >= temp_list[i]:
                    max_val = temp_list[i]
                elif temp_list[i] == max_val and lst.count(temp_list[i]) >= max_freq:
                    max_freq = lst.count(temp_list[i])
                    max_val = temp_list[i]
        if max_val == -1:
            return -1
        else:
            return max_val


