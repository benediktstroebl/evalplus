
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    #iterating through the list
    result = 0
    for index, element in enumerate(lst):
        #checking for odd
        if index % 2 != 0:
            #checking if the element is odd
            if element % 2 != 0:
                #adding odd elements which are in odd index
                result += element
    return result
