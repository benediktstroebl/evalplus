
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    result = 0
    for index in range(0,len(lst),2):
        result += lst[index]
    return result
    #check
    #a = solution([5, 8, 7, 1])
    #print(a)
    #assert(a == 12)
    
    #a = solution([3, 3, 3, 3, 3])
    #print(a)
    #assert(a == 9)
    #a = solution([30, 13, 24, 321])
    #print(a)
    #assert(a == 0)
    
    #a = solution([10, 18, 5, 2, 7])
    #print(a)
    #assert(a == 5)
    print('done')
