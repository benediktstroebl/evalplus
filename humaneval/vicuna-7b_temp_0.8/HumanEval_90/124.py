
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if not lst:
        return None
    else:
        left = 1
        right = 1
        while left < len(lst):
            while right < len(lst) and lst[right] < lst[left]:
                right += 1
            while left < len(lst) and lst[left] > lst[right]:
                left += 1
            if left < len(lst) and lst[left] < lst[right]:
                if right == len(lst) - 1:
                    return lst[left]
                if left == 1:
                    return lst[right]
                while left < len(lst) and lst[left] > lst[right]:
                    left += 1
            right = len(lst)
        return None
