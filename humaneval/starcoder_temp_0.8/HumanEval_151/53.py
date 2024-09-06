
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
    if lst == []:
        return 0
    else:
        new_list = []
        for i in range(len(lst)):
            if lst[i]%2!= 0:
                new_list.append(lst[i])
        square_list = [i**2 for i in new_list]
        return sum(square_list)
