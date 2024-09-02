
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0)
    return sum([n for (i, n) in enumerate(lst) if (i + 1) % 2 == 0 and n % 2 != 0])

    # 바꿔보기
    # return sum(lst[i] for i in range(0, len(lst), 2) if i % 2 != 0 and lst[i] % 2 != 0)
    # return sum(lst[i] for i in range(0, len(lst), 2) if i % 2 == 0 and lst[i] % 2 != 0)

    # 바꿔보기2
    # return sum(lst[i] for i in range(len(lst)-1) if i % 2 == 0 and lst[i] % 2 != 0)
    # return sum(lst[i] for i in range(len(lst)) if i % 2 !=
