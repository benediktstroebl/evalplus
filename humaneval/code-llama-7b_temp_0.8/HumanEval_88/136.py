
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Check edge case
    if not array or len(array) == 1:
        return array

    # Define the 2 dicts
    # odds is to store the odd index value
    odds = dict()
    # evens is to store the even index value
    evens = dict()
    # Store the sum of the 1st and last index of array
    sum_last_first = sum(array)

    # Odd case: even numbers
    if sum_last_first % 2 == 0:
        for index in range(len(array)):
            if index % 2 == 0:
                evens[index] = array[index]
            else:
                odds[index] = array[index]
        # Resort the odds dict based on the value
        return sorted(odds, key=odds.get) + sorted(evens, key=evens.get)

    # Even case: odd numbers
    elif sum_last_first % 2 != 0:
        for index in range(len(array)):
            if index % 2 == 0:
                evens[index] = array[index]
            else:
                odds[index] = array[index]
        # Resort the evens dict based on the value
        return sorted(evens, key=evens.get) + sorted(odds, key=odds.get)





















