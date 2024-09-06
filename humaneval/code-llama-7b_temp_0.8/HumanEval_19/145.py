from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # split string into array
    num_array: List[str] = numbers.split(' ')
    # create new empty array for results
    num_results: List[str] = []
    # loop through each element in array
    for i in num_array:
        # set default smallest number
        smallest_num = 10
        # loop through each element again
        for j in num_array:
            # if current element is less than smallest number
            if j < smallest_num:
                # make current element smallest number
                smallest_num = j
        # remove smallest number from array
        num_array.remove(smallest_num)
        # append smallest number to results
        num_results.append(smallest_num)
    # return sorted array
    return ' '.join(num_results)

