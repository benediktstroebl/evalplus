
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
    # Using a list comprehension to create a new list
    # containing all possible permutations of the digits
    # from 0 to 9
    digits = [str(d) for d in range(10)]
    permutations = [d for digits_ in digits for d in digits_]
    permutations_lst = list(permutations)

    # Using the built-in python function to get the index of a element
    index_of = lambda x: [i for i, d in enumerate(permutations_lst) if x == d][0]

    # Using the built-in python function to get the number of times
    # an element appears in the list
    frequency = lambda x: [i for i, d in enumerate(permutations_lst) if x == d][0]

    # Using the built-in python function to get the sorted list of numbers
    sorted_lst = sorted(permutations_lst, key=lambda x: sum(int(d) for d in x))

    # Using the index_of and frequency functions to extract
    # the index and frequency of the elements in the sorted_lst
    sorted_lst = [sorted_lst[index_of(num)] for num in nums]

    # Extracting the original list from the sorted_lst
    return sorted_lst