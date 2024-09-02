
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odds = []
    for item in lst:
        if item%2 == 1:
            odds.append(item)
    if not odds:
        return 0
    else:
        return sum(odds[::2])
        

