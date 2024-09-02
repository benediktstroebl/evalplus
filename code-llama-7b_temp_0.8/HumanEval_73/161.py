
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
    if len(arr) < 2:
        return 0
    n = len(arr)
    # initialize table[i][j] to max(n - min(i, j))
    #table = [[n for j in range(n)] for i in range(n)]
    table = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        table[i][i] = 0
    # set diagonal element
    for i in range(n - 1):
        table[i][i + 1] = 1
    # set table[i][j] to table[i + 1][j - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 2, n):
            table[i][j] = table[i + 1][j - 1]

    #print_table(table)
    for i in range(n):
        for j in range(i + 2, n):
            table[i][j] = min(
                table[i][j],
                table[i + 1][j - 1] + 1)
            table[i][j] = min(
                table[i][j],
                table[i][j - 1] + 1)

    #print_table(table)
    return n - min([n - table[i][n - 1] for i in range(n)])

