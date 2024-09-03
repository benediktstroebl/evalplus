def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    :arr: list of integers
    :k: integer

    Returns: sum of elements with at most two digits
    """
    # Include the first element in the sum
    return sum([x for x in arr[:k] if len(str(x)) <= 2])