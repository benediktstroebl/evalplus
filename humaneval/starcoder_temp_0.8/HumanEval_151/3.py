
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
    # My solution
    # new_lst = []
    # for i in lst:
    #     if i % 2 == 0:
    #         new_lst.append(i)
    # total = 0
    # for num in new_lst:
    #     total += num ** 2
    # return total
    #----------------------------------
    # Harvard solution
    return sum([x ** 2 for x in lst if x % 2!= 0])
