
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # Use this array to keep track of the sums
    sums = []

    for i in range(0, len(lst)):
        # if the number is odd and it's in an even position
        if lst[i] % 2 != 0 and i % 2 == 0:
            sums.append(lst[i])

    # return the sum of the numbers in the sums array
    return sum(sums)
