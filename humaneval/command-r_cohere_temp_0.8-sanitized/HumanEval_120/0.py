def maximum(arr, k):
    """
    Returns the maximum k numbers from the given array.

    Args:
        arr (list): A list of integers.
        k (int): Number of maximum elements to return.

    Returns:
        list: A sorted list containing the maximum k numbers from the input array.
    """
    max_k_nums = sorted(arr)[-k:]
    return max_k_nums