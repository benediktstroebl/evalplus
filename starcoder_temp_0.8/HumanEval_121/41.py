
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Step 1:
    # make an empty list to append odd integers that are in even positions
    
    # Step 2:
    # create a for loop to iterate through the list
    
    # Step 3:
    # add the odd integers in even positions to a new list
    odd_list = [x for x in lst if x % 2!= 0]
    
    # Step 4:
    # add the sum of the numbers in the new list
    sum_odd_list = sum(odd_list)
    
    # Step 5:
    # return sum_odd_list
    return sum_odd_list
    
