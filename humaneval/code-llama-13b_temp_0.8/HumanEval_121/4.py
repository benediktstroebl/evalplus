
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    evens = []
    for i, val in enumerate(lst):
        if i % 2 != 0:
            evens.append(val)
    sums = 0
    for num in evens:
        if num % 2 != 0:
            sums += num
    return sums

