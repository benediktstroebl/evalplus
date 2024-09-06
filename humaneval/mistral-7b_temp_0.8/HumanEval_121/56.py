
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # input.append(0)
    # input.insert(0, 0)
    # for i in range(1, len(input), 2):
    #     input[i] += input[i - 1]
    # return input[-1]
    # ----------------------------------------------
    input.append(0)
    input.insert(0, 0)
    for i in range(1, len(input), 2):
        input[i] += input[i - 1]
    return input[-1]

