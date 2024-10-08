def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    arr.sort(reverse=True)
    return arr[:k]
