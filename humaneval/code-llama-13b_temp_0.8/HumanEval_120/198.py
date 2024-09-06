
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """

    def get_partition_indices(arr, k):
        sorted_arr = sorted(arr, reverse=True)
        return sorted_arr[ : k]

    def get_frequency(arr, k):
        return dict(collections.Counter(arr))

    def get_maximum_k_numbers(arr, k):
        frequency = get_frequency(arr, k)
        partition_indices = get_partition_indices(arr, k)
        output = [0] * len(partition_indices)
        for index, partition_index in enumerate(partition_indices):
            output[index] = frequency[partition_index]
            frequency[partition_index] = 0
        return output

    return get_maximum_k_numbers(arr, k)

