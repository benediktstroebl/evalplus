
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # T: O(n)
    # DFS, track the sum of elements in each iteration, return the sum of odd elements in even positions
    for i in range(len(lst)-1):
        sum = 0
        for j in range(i, len(lst)):
            if j%2 == 0:
                continue
            sum += lst[j]
        return sum
