
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0
    odd_index = [0]
    even_index = [0]
    for i, num in enumerate(lst):
        if num % 2 == 0:
            even_index.append(i + 1)
        else:
            odd_index.append(i + 1)
    for i in range(len(even_index)):
        lst[even_index[i]] = 0
    return sum([num for num in odd_index for i in range(len(even_index)) if odd_index[i] != i and num % 2 != 0])