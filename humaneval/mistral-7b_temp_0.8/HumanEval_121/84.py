
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # TODO: Write your solution here
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    if even > 0:
        return odd*2
    else:
        return 0

