
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    even_position = []
    odd_position = []
    
    for i in range(len(lst)):
        if i % 2 == 0:
            even_position.append(lst[i])
        else:
            odd_position.append(lst[i])
    
    total = 0
    for i in range(len(even_position)):
        total += odd_position[i]
    return total
