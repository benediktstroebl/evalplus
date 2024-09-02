
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # Try to solve this without using filter, but also write a version with filter
    # What else can you change?

    # 1st try
    # return sum(x for x in lst if x % 2 == 1 and (x + 1) % 2 == 0)

    # 2nd try
    return sum([x for i, x in enumerate(lst) if x % 2 == 1 and i % 2 == 0])
