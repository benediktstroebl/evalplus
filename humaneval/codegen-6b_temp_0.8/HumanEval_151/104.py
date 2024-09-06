
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
    # print(lst)
    if not lst:
        return 0
    for i in range(len(lst)-1):
        if lst[i] % 2 != 0:
            lst[i] = lst[i] * lst[i]
    lst.reverse()
    for i in range(len(lst)-1):
        if lst[i] % 2 != 0:
            return lst[i] + lst[i+1]
    return 0

assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([0, 0]) == 0
assert double_the_difference([1, 3, 0]) == 1
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([0, 5, 1]) == 5
assert double_the_difference([0, -1, 3]) == 1
assert double_the_difference([]) == 0
