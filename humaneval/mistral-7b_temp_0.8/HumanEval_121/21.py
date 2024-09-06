
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # your code goes here
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    evens = 0
    odds = 0

    for i, x in enumerate(lst):
        if i % 2 == 0:
            evens += x

        if i % 2 == 1:
            odds += x

    if odds > evens:
        return evens + odds
    else:
        return evens
