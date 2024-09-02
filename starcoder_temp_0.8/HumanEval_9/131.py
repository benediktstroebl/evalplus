from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # We are going to use a stack to manage the rolling maximum
    stack = [numbers[0]]
    max_list = [numbers[0]]
    for number in numbers[1:]:
        # We want to keep pushing new numbers that are equal or larger than the
        # number in the top of the stack.
        # We can do it by checking the last element of the stack.
        if number >= stack[-1]:
            stack.append(number)
        else:
            # Otherwise, we want to find the maximum element between the number
            # that just popped and the number we are currently looking at.
            # This maximum is the new number to be added.
            max_list.append(max(stack.pop(), number))
            stack.append(max_list[-1])
    return max_list

