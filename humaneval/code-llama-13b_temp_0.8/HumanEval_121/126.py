
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # result = []
    # for i in range(0, len(lst), 2):
    #     if i % 2 == 0:
    #         result.append(lst[i])
    # print(sum(result))
    
    # print(sum([x for i, x in enumerate(lst) if x % 2 == 0 and i % 2 == 1]))
    
    # filter_even = lambda x : x % 2 == 0
    # filter_odd = lambda x : x % 2 != 0
    # even_indexes = filter(filter_even, lst)
    # odd_indexes = filter(filter_odd, lst)
    # print(sum(list(odd_indexes)))
    
    # print(sum([lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 1]))
    print(sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 1]))
    
    # return sum(filter(lambda x: x % 2 == 0, list(filter(lambda x: x % 2 == 1, lst))))


