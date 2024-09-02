from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # sort the input list
    numbers.sort()

    # initialize a variable to keep track of the latest maximum element
    latest_max = numbers[-1]

    # initialize a variable to store the length of the latest maximum
    max_len = 1

    # initialize a variable to store the latest maximum list
    latest_max_list = [latest_max]

    # start with the current element
    current_num = numbers.pop(0)

    for i in range(1, len(numbers)):
        # append the current element to the latest maximum list
        latest_max_list.append(current_num)

        # check if the new element is greater than the latest maximum element
        if current_num > latest_max:
            # update the latest maximum element and latest maximum length
            latest_max = current_num
            max_len = 1

        # check if we've reached the end of the sequence
        if len(latest_max_list) >= max_len:
            # add the latest maximum list to the output list
            output_list = []
            for num in latest_max_list:
                output_list.append(num)
            output_list.append(latest_max)

            # remove the latest maximum list from the latest maximum list
            latest_max_list.pop()

            # update the latest maximum element and latest maximum length
            latest_max = current_num
            max_len += 1

        # remove the current element from the input list
        numbers.pop(0)

    return output_list

