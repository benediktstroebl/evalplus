
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    if not arr:
        return 0

    N = len(arr)
    if N == 1:
        return 0
    if N == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 2

    # f(i, j) = min {f(i+1, j), f(i, j-1), f(i+1, j-1) + 1} + 1
    # f(i, j) = f(i+1, j) + 1
    # f(i, j) = f(i, j-1) + 1
    # f(i, j) = f(i+1, j-1) + 1
    # f(i, j) = f(i+1, j-1) + 1
    # f(i, j) = f(i+1, j-1) + 1

    table = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        table[i][i] = 0
    for i in range(N-1):
        if arr[i] == arr[i+1]:
            table[i][i+1] = 0
        else:
            table[i][i+1] = 1

    for size in range(3, N+1):
        for i in range(N):
            j = i + size - 1
            if j >= N:
                continue
            min_cost = min(table[i+1][j], table[i][j-1], table[i+1][j-1]) + 1
            if arr[i] == arr[j]:
                min_cost = min(min_cost, table[i+1][j-1])
            table[i][j] = min_cost

    return table[0][-1]

