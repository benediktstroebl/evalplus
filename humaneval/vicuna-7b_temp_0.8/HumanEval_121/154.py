
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Tries to iterate through all elements of the list and check if it is odd, if so, increment the counter
    counter = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            counter += lst[i]
    return counter
