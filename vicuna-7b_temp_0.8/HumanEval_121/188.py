
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    n = len(lst)
    sum = 0
    for i in range(n-1):
        if lst[i] % 2 == 0 and lst[i+1] % 2 != 0:
            sum += lst[i]
    return sum


test = [
[5, 8, 7, 1],
[3, 3, 3, 3, 3],
[30, 13, 24, 321],
[3, 4, 10, 1],
[3, 5, 11, 8],
[3, 5, 7, 10, 9, 4],
[4, 9, 1, 8, 5, 10, 7],
[2, 3, 5, 7, 1, 9, 4],
[3, 2, 5, 6, 7, 8],
[1, 2, 3, 4, 5, 6, 7, 8],
[1, 2, 4, 3, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[3, 1, 5, 7, 9, 11, 13, 15],
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[1, 2, 3, 4, 5, 6, 7
