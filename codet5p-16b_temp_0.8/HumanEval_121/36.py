
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    odd_number = []
    sum = 0
    
    for num in range(len(lst)):
        if num % 2 == 0:
            odd_number.append(lst[num])
    
    for i in odd_number:
        sum += i
    
    return sum
