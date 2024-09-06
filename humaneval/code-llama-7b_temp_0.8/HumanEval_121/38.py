
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # position 0: 5
    # position 1: 8
    # position 2: 7
    # position 3: 1

    # odd position: 1
    # even position: 0

    # odd values: 5, 1

    odd_values = []

    for position, element in enumerate(lst):
        if (position + 1) % 2 == 0:
            if element % 2 == 1:
                odd_values.append(element)

    return sum(odd_values)

