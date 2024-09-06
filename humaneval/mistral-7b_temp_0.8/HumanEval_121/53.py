
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Find the sum of all the odd elements
    oddSum = sum(lst[i] for i in range(len(lst)) if lst[i] % 2 != 0)
    # Find the sum of the even positions
    evenSum = sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 0)
    # Multiply the two sums
    result = oddSum * evenSum
    # Return the result
    return result












































































































































