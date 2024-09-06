
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    # Your code here
    # empty list
    if len(lst) == 0:
        return 0
    
    # if the list has only one element and it is not a number
    if len(lst) == 1 and not isinstance(lst[0], int):
        return 0
    
    # if the first element is not a number
    if not isinstance(lst[0], int):
        lst.pop(0)
    
    # remove the negative element and their absolute value
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            lst.pop(i)
    
    # list comprehension
    return sum([abs(i) ** 2 for i in lst if i % 2 != 0])



