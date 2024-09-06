
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
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
    
    # Solution
    # def next_smallest(lst):
    #     if len(lst) < 2:
    #         return None
        
    #     lst.sort()
    #     for i in range(len(lst)):
    #         if lst[i] < lst[i+1]:
    #             return lst[i+1]
        
    #     return None
    
    # An alternative solution
    # def next_smallest(lst):
    #     if len(lst) < 2:
    #         return None
    #     lst = sorted(lst)
    #     for i in range(1, len(lst)):
    #         if lst[i] != lst[i - 1]:
    #             return lst[i]
    #     return None
    
    # An alternative solution
    # def next_smallest(lst):
    #     if len(lst) < 2:
    #         return None
    #     lst = sorted(lst)
    #     for i in range(1, len(lst)):
    #         if lst[i] != lst[i - 1]:
    #             return lst[i]
    #     return None
    
    # Test
    # import random
    # for i in range(1000):
    #     lst = [random.randint(1, 1000) for i in range(random.randint(0, 100))]
    #     sol = next_smallest(lst)
    #     if sol and sol < sorted(lst)[1]:
    #         print(lst)
    #     assert next_smallest(lst) == next_smallest2(lst)
    
    # Test 2
    # import random
    # for i in range(1000):
    #     lst = [random.
