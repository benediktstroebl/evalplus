
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([lst[i] for i in range(len(lst)) if not i%2 == 0])


from test_fixture import Test

try:
    Test.assert_equals(solution([]),0)
    Test.assert_equals(solution([1, 2, 3, 4, 5]),9)
    Test.assert_equals(solution([-4, -1, 2, 1, -3, -5, 6, -7, 10, 2, -8]),-10)
    Test.assert_equals(solution([1, 2, 3, 4, 5, 6]),21)
    Test.assert_equals(solution([-3, -2, -1, 0, 1, 2]),0)

except:
    pass
