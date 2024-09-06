
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 if lst[i] % 2 == 1])


from test_fixture import TestFixture

tf = TestFixture(solution)
tf.add_list(list(range(10)))
tf.add_list(list(range(100, 200, 2)))
tf.add_list(list(range(100, 200, 3)))
tf.add_list([3, 3, 3, 3, 3])
tf.add_list([30, 13, 24, 321])
tf.add_list([])
tf.add_list([12, 3, 5, 7, 9])
tf.add_list([2, 1])
tf.add_list([2, 1, 3, 3, 5])
tf.add_list([5, 8, 7, 1])
tf.add_list([10, 3, 4, 6, 8, 5, 3, 1, 7, 2, 4, 8])
tf.execute()
