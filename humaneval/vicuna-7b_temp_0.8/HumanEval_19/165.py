from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a list of lists of strings
    number_list = [['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]

    # Define a dictionary that maps each string to its index in the list
    string_to_index = {i: i for i in number_list[0]}

    # Iterate through the list of strings
    for s in number_list[1:]:
        for i, n in enumerate(s):
            string_to_index[n] = i + 1

    # Define a dictionary that maps each string to its value
    value_dict = {i: str(j) for i, j in string_to_index.items()}

    # Sort the list of strings using the Counter from the Counter class in the Counter module in the collections
    sorted_value_dict = Counter(value_dict.values())

    # Define a list of strings containing the sorted values
    sorted_values = [sorted_value_dict[i] for i in sorted_value_dict]

    # Join the sorted values back into a single string
    return ' '.join(sorted_values)
