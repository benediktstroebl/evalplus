
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # your code here

    odd_sum = 0
    even_pos = 0

    for x in lst:
        if x % 2 != 0:
            odd_sum += x
        elif x % 2 == 0 and even_pos % 2 == 0:
            odd_sum += x
        even_pos += 1

    return odd_sum
