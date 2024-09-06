
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # best_arrangement = []
    # for i in range(len(arr) - 1):
    #     if arr[i] <= arr[i + 1]:
    #         best_arrangement.append(arr[i])
    # return best_arrangement

    # if all elements of array are negative, then no solution
    if all(x < 0 for x in arr):
        return -1

    # if first element is negative, solution is first element
    if arr[0] < 0:
        return 0

    # index of first positive element
    first_positive = 0

    # find first positive element
    for i in range(len(arr)):
        if arr[i] >= 0:
            first_positive = i
            break

    # sum of elements upto index of first positive element
    sum_to_first_positive = sum(arr[:first_positive + 1])

    # if sum is 0, return first positive element
    if sum_to_first_positive == 0:
        return first_positive

    # store diff in sum till last positive element
    sum_diff = {first_positive: sum_to_first_positive}

    # find the last positive element
    for i in range(first_positive + 1, len(arr)):
        # update the sum_diff
        sum_to_first_positive -= arr[i - 1]
        sum_to_first_positive += arr[i]
        sum_diff[i] = sum_to_first_positive
        # return the index if sum_to_first_positive is 0
        if sum_to_first_positive == 0:
            return i
    # if no solution, return -1
    return -1

