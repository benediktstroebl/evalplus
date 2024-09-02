
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # A linear time solution using two pointers
    # One pointer starts at the beginning, and the other starts at the end
    # At each iteration, the pointer at the end is decremented by one,
    # and the sum of the elements in the range between the pointers is returned
    # If the current element is odd and in an even position, it is added to the sum
    # If the current element is odd and in an odd position, the solution is already correct,
    # and if the current element is even and in an odd position, the solution is already correct
    sum = 0
    odd_lst = [x for x in lst if x % 2 != 0]
    for i in range(len(lst)-1):
        sum += lst[i]
        if lst[i] % 2 != 0 and i % 2 == 1:
            sum += lst[i+1]
    return sum
