
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    left = 0
    right = len(lst)-1
    while left <= right:
        while left < right and lst[left] % 2 == 0:
            left += 1
        if left >= right:
            break
        odd = lst[left] % 2
        if odd == 0:
            left += 1
        else:
            sum = left + 1
            if sum < right:
                right = sum
            odd_sum = sum
            while odd_sum < right:
                odd_sum += 2
            lst[left:right] = [lst[left], odd_sum]
            while odd_sum < right and odd_sum % 2 == 0:
                odd_sum += 2
            left = right + 1
    return sum
