
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    if type(lst) is not list:
        return "Argument is not a list."
    if len(lst) == 0:
        return "Empty list."
    if len(lst)!= len(lst):
        return "Invalid length of the list."
    if len(lst) == 1:
        return "Invalid length of the list."
    else:
        sum = 0
        for i in range(len(lst)):
            if i % 2 == 0:
                sum = sum + lst[i]
        return sum

