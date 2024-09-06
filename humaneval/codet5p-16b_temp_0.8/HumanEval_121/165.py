
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    
    l = []
    l1 = []
    for i in range(len(lst)):
        if i%2 == 0:
            l1.append(lst[i])
        else:
            l.append(lst[i])
    for i in l:
        if i in l1:
            l1.remove(i)
    return sum(l1)
