
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
    # your code

    signs = set()
    for n in arr:
        signs.add(n / abs(n))
    if signs == {1}:
        return sum(arr)
    if signs == {-1}:
        return sum(arr[i] if i % 2 else -arr[i] for i in range(len(arr)))
    if signs == {1, -1}:
        return sum(arr[i] if i % 2 else -arr[i] for i in range(len(arr))) * len(arr)
    if signs == {0}:
        return 0
    return None

