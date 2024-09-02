
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    list1=[]
    list2=[]
    for i in lst:
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
    return sum(list1) + sum(list2)
    
assert(solution([5, 8, 7, 1]) == 12)
assert(solution([3, 3, 3, 3, 3]) == 9)
assert(solution([30, 13, 24, 321]) == 0)
assert(solution([10, 4, 7, 1]) == 0)
assert(solution([5,2,3,4,1,9,8,7]) == 0)

