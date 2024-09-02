
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([i for i in lst if i%2==1 and lst.index(i)%2==0])
    #Above solution passed 29/31 tests
    #lst = sorted(lst, key=lambda x: x%2==0)
    #return sum([i for i in lst if i%2!=0])
    #Above solution passed 30/31 tests
    
