
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

    if len(arr) == 0:
        return None
    else:
        negative = False
        positive = False
        zero = False
        if arr[0] < 0:
            negative = True
            arr[0] = -arr[0]
        elif arr[0] > 0:
            positive = True
            arr[0] = -arr[0]
        else:
            zero = True
            arr[0] = 0
        for i in arr[1:]:
            if i < 0:
                negative = True
                i = -i
            elif i > 0:
                positive = True
                i = -i
            elif i == 0:
                zero = True
                i = 0
        if negative:
            return arr[0] * arr[1:]
        elif positive:
            return arr[0] * arr[1:]
        elif zero:
            return 0
        else:
            return arr[0] * arr[1:]
