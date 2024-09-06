
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # lst.index(321)
    sum_lst = 0
    even_index = 0
    # print(lst[even_index])
    for i in lst:
        if i % 2 == 1 and even_index % 2 == 0:
            sum_lst += i
            # print("index: ", even_index)
        even_index += 1
        # print(even_index)
    return sum_lst

