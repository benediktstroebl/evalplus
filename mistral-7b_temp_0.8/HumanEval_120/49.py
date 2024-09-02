
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

    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    def find_largest_k_numbers(arr, k):
        # create an empty list to store the maximum k numbers
        max_k_numbers = []

        # sort the array in descending order
        sorted_arr = sorted(arr, reverse=True)

        # iterate through the sorted array and add the maximum k numbers to the list
        for i in range(k):
            max_k_numbers.append(sorted_arr[i])

        # return the list of maximum k numbers
        return max_k_numbers

    # print(find_largest_k_numbers([-3, -4, 5], 3))  # [-4, -3, 5]
    # print(find_largest_k_numbers([4, -4, 4], 2))  # [4, 4]
    # print(find_largest_k_numbers([-3, 2, 1, 2, -1
