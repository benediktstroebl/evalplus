
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Using a dictionary to keep track of the count of each number in the range [0, n)
    count = {i: 0 for i in range(1, len(lst) + 1)}
    for i in range(1, len(lst) + 1):
        count[i] += 1
        
    # Traversing the list and finding the odd numbers in even positions
    sum = 0
    for i, val in enumerate(lst):
        if val % 2 != 0:
            sum += val
            count[val // 2] -= 1
            count[val // 2] += 1
            break
        
    return sum
