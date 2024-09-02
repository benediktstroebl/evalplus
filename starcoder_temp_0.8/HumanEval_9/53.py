from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # The easiest way to solve this problem is to traverse the input array and compare each value with the
    # element from previous position. If the value is greater, we will replace the value.
    # For example:
    #   given:
    #     [1, 2, 3, 2, 3, 4, 2]
    #
    #   we will compare first element with second one:
    #     [1, 2, 3, 3, 3, 4, 4]
    #
    #   then we will compare the second element with the third one:
    #     [1, 2, 3, 3, 3, 4, 4]
    #
    #   and so on...
    #
    # So, our approach will be:
    #   1) Create an output array. The size of this array is the same as input array.
    #   2) For each element of the input array:
    #       a) If this element is greater than previous, then the output array should contain this element
    #          instead of previous.
    #       b) Otherwise, the output array should contain the previous element.

    # So, the size of the output array is the same as input array
    output: List[int] = [0] * len(numbers)

    # The maximum value seen so far
    maximum_value_seen_so_far = numbers[0]

    # Now, we can iterate over the input array and determine the maximum value seen so far
    for i in range(len(numbers)):
        # Check if the current element is greater than maximum value seen so far
        if numbers[i] > maximum_value_seen_so_far:
            # If it is, then update the maximum value seen so far
            maximum_value_seen_so_far = numbers[i]

        # Add the maximum value seen so far to the output array
        output[i] = maximum_value_seen_so_far

    return output

