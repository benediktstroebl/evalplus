
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

    #print(lst)
    if lst:
        lst = [int(i) for i in lst]
        x = [i for i in lst if i % 2 == 1]
        y = [i for i in lst if i % 2 == 0]
        x = [i*i for i in x]
        y = [i*i for i in y]
        #print(x)
        #print(y)
        #print(sum(x))
        #print(sum(y))
        return sum(x) - sum(y)
    else:
        return 0
