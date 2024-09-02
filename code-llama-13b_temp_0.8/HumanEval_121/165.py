
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    answer = 0
    odds = list()
    for i, number in enumerate(lst):
        if number % 2 != 0:
            odds.append(number)
    if len(odds) > 0:
        if len(odds) % 2 == 0:
            for i in range(0, len(odds)):
                if i % 2 == 0:
                    answer += odds[i]
        else:
            for i in range(0, len(odds) - 1):
                if i % 2 == 0:
                    answer += odds[i]
    return answer
