def sort_array(arr):
    """
    Sorts the array of integers based on the number of ones in their binary representation in ascending order.
    return: array sorted in ascending order
    """
    bin_arr = [int(bin(num)[2:]) for num in arr]
    return sorted(arr, key=lambda x: -bin_arr[x])
arr = [1, 5, 2, 3, 4]