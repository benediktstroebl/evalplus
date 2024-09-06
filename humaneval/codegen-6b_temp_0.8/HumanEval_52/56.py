

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    def helper(num, threshold):
        if num < threshold:
            return True
        return False
    
    return all(helper(num, t) for num in l)
