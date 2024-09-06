
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd = [n for n in lst if n % 2 == 1]
    even = [n for n in lst if n % 2 == 0]
    #print (odd, even)
    result = 0
    for i in range(0, len(odd), 2):
        result += odd[i]
    return result

