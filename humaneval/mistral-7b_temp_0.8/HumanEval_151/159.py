
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
    # your code here
    #print(lst)
    #print(list(filter(lambda x: isinstance(x, int), lst)))
    #print(list(filter(lambda x: x % 2 == 1, list(filter(lambda x: isinstance(x, int), lst)))))
    #print(list(map(lambda x: x * x, list(filter(lambda x: x % 2 == 1, list(filter(lambda x: isinstance(x, int), lst)))))))
    #return sum(list(map(lambda x: x * x, list(filter(lambda x: x % 2 == 1, list(filter(lambda x: isinstance(x, int), lst)))))))

    return sum(map(lambda x: x**2, filter(lambda x: x%2 == 1 and isinstance(x, int), lst)))
