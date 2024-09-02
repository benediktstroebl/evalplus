
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    #Explanation
    #The sum of all the odd elements that are in even positions is the same as the sum of all the odd elements minus the sum of all the even elements in odd positions.
    return sum(lst) - sum(filter(lambda x: x%2 == 1, lst[::2]))
