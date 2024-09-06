
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # IMPORTANT: use the function 'sum' and 'list comprehension'
    
    # The best solution is:
    return sum([lst[i] for i in range(0, len(lst), 2)])
    
    # Other solutions:
    # return sum([lst[i] for i in range(0, len(lst)) if lst[i] % 2 == 1 and i % 2 == 0])
    # return sum([lst[i] for i in range(len(lst)) if lst[i] % 2 == 1 and i % 2 == 0])
    # return sum([lst[i] for i in range(len(lst)) if lst[i] % 2 and not i % 2])
    # return sum([lst[i] for i, x in enumerate(lst) if x % 2 and not i % 2])
    # return sum([lst[i] for i, x in enumerate(lst) if x % 2 and i % 2 == 0])
    # return sum([x for i, x in enumerate(lst) if x % 2 and i % 2 == 0])
    # return sum([x for i, x in enumerate(lst) if not x % 2 and i % 2])
    # return sum([x for i, x in enumerate(lst) if not x % 2 and i % 2 == 1])
    # return sum([x for i, x in enumerate(lst) if x % 2 and not i % 2])
    # return sum([x for i, x in enumerate(lst) if x % 2 and i % 2 == 1])
    # return sum([x for i, x in enumerate(lst) if x % 2 and not i % 2])
    # return sum([x for i, x in enumerate(lst) if x % 2 and i % 2 == 1])
    # return sum([x for i, x in enumerate(lst) if x % 2 and i % 2 == 1])
    # return sum([x for i, x in enumerate(lst) if x % 2 and i % 2 == 0])
    # return sum([
