
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # FIXME: This is way too slow.
    #
    # # Get an array of items with # of ones.
    # ones = [0] * 32
    # for num in arr:
    #     for i in range(32):
    #         if num & (1 << i):
    #             ones[i] += 1
    #
    # # Get the index of the ones array.
    # indices = [i for i in range(len(ones)) if ones[i] != 0]
    #
    # # Sort the array.
    # sorted_ones = [0] * len(ones)
    # while len(ones) != 0:
    #     min_idx = ones.index(min(ones))
    #     min_ones = ones[min_idx]
    #     for i in range(min_ones):
    #         sorted_ones[i] = ones[min_idx]
    #     ones = ones[:min_idx] + ones[min_idx + 1:]
    #
    # return sorted_ones

    # FIXME: This is way too slow.
    #
    # # Get an array of items with # of ones.
    # ones = [0] * 32
    # for num in arr:
    #     for i in range(32):
    #         if num & (1 << i):
    #             ones[i] += 1
    #
    # # Get the index of the ones array.
    # indices = [i for i in range(len(ones)) if ones[i] != 0]
    #
    # # Sort the array.
    # sorted_ones = [0] * len(ones)
    # while len(ones) != 0:
    #     min_idx = ones.index(min(ones))
    #     min_ones = ones[min_idx]
    #     for i in range(min_ones):
    #         sorted_ones[i] = ones[min_idx]
    #     ones = ones[:min_idx] + ones[min_idx + 1:]
    #
    # return sorted_ones

