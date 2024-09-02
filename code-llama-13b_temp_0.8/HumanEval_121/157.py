
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    #checking type of input
    if not isinstance(lst, list):
        return 'not a list'
    
    #if len of list is less than 1 return 0
    if len(lst) < 1:
        return 0
    
    else:
        # setting variable to zero
        sum = 0
        
        # looping over length of lst and adding only the elements where index is even and value is odd
        for i in range(len(lst)):
            if i % 2 == 0 and lst[i] % 2 == 1:
                sum += lst[i]
        
        # return the sum
        return sum
