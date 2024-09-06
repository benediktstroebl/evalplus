
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Your code here

    # Step 1: set an odd_sum variable equal to 0.
    # Step 2: use the len() function to get the length of the list.
    # Step 3: for each element of the list starting at index 1:
    #          If the element is odd and the index of the element is even:
    #              1. Add the element to the odd_sum variable.
    #          Otherwise, don't do anything.
    # Step 4: return the odd_sum variable.

    odd_sum = 0
    length = len(lst)
    for i in range(1, length):
        if lst[i] % 2 != 0 and i % 2 == 0:
            odd_sum += lst[i]
    return odd_sum
