
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    # if not nums:
    #     return []

    # # Convert each number into a list of their digits
    # # For example:
    # # >>> nums_to_digits([123, 456]) == [[1, 2, 3], [4, 5, 6]]
    # nums_to_digits = lambda x: [int(d) for d in str(x)]

    # # Create a dictionary of the items and their corresponding sum of digits
    # # For example:
    # # >>> nums_to_points([123, 456]) == {123: 6, 456: 15}
    # nums_to_points = lambda x: {i: sum(nums_to_digits(i)) for i in x}

    # # Create a dictionary where the key is the sum of digits and the value is the list of items
    # # For example:
    # # >>> nums_to_points([123, 456]) == {6: [123], 15: [456]}
    # d = {d: [] for d in map(lambda x: nums_to_points(x).values(), nums)}

    # # Fill in the dictionary with items and their corresponding sum of digits
    # # For example:
    # # >>> nums_to_points([123, 456]) == {6: [123], 15: [456]}
    # for i, n in enumerate(nums):
    #     d[nums_to_points(n).values()].append(n)

    # # Create a sorted list of the items by their corresponding sum of digits
    # # For example:
    # # >>> nums_to_points([123, 456]) == [456, 123]
    # res = []
    # for lst in sorted(d.values()):
    #     res += lst

    
