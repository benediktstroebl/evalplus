
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    min_num = float("inf")
    lst_of_nums = []
    for num in lst:
        if num < min_num:
            min_num = num
        elif num not in lst_of_nums:
            lst_of_nums.append(num)

    if lst_of_nums == []:
        return None
    else:
        for num in lst_of_nums:
            if num < min_num:
                min_num = num
    return min_num
