
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
        sum = 0
        for num in arr:
            signs = [1 if n == num else -1 if n < num else 0 for n in arr]
            signs = [s if s == 1 else -s if s == -1 else 0 for s in signs]
            sign_product = sum(signs)
            magnitude = sum([abs(n) for n in arr])
            sign_mag = sign_product * magnitude
            if sign_mag == 1:
                sum += magnitude
            elif sign_mag == 0:
                if sum[-1] == -1:
                    sum += magnitude
            else:
                if sum[-1] == 1:
                    sum += magnitude
                else:
                    sum += abs(magnitude)
        return sum
