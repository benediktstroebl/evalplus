
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    #Initialize the sum
    sum = 0
    
    #Iterate over the list
    for i in range(len(lst)):
        #If the index is even, check if the value is odd and add it to the sum
        if i % 2 == 0:
            if lst[i] % 2 == 1:
                sum += lst[i]
            
    return sum
        
