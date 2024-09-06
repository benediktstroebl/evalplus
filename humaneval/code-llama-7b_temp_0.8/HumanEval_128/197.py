
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    # your code here
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    arr_map = [str(x) for x in arr]
    temp = ["0"] * len(arr)
    for i in range(len(arr_map)):
        if arr_map[i][0] == "-":
            arr_map[i] = arr_map[i][1:]
            temp[i] = "-"
        elif arr_map[i][0] == "0":
            arr_map[i] = "0"
            temp[i] = "0"
        else:
            temp[i] = "1"
    temp = "".join(temp)
    arr = [int(i) for i in arr_map]
    arr_prod = 1
    for i in arr:
        arr_prod *= i
    if temp == "0":
        return 0
    if temp == "-0":
        return 0
    return arr_prod * int(temp)

