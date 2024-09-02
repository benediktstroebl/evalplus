
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # My and best way solution
    odds = []
    for index in range(len(lst)):
        if index % 2 == 1:
            odds.append(lst[index])
    return sum(odds)


    # Best way solution
    return sum(i for i in lst if not i % 2)

