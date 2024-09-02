
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # check if the list is empty
    if not lst:
        return 0

    # check if the last element is odd
    if lst[-1] % 2 == 1:
        return lst[-1]

    # check if the last element is the only odd element
    if lst[-1] == (lst[-1] // 2) * 2 + 1:
        return lst[-1]

    # find the index of the last odd element
    last_odd = len(lst) - 1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 1:
            last_odd = i
            break

    # get the sum of all odd elements that are in even positions
    sum = 0
    for i in range(last_odd, 0, -1):
        sum += lst[i]

    return sum
