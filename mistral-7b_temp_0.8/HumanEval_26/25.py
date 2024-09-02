from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Hint: use the method List.remove.
    # To remove an element from a list, use the method List.remove(element).
    # The method will remove the first instance of element from the list.
    # If the list is empty, the method will raise a ValueError.
    # Note that remove_duplicates should return a list of integers.
    # We'll use a for-loop to iterate through the list.
    # We'll use a counter to keep track of the number of times each number occurs.
    # We'll use a set to store the numbers that have been removed.
    # We'll use a while-loop to keep iterating until we've removed all the duplicates.

    output = []
    counter = 0
    numbers_left = numbers
    for number in numbers_left:
        if number not in output:
            output.append(number)
            counter = 1
        else:
            if counter == 1:
                counter = 0
                numbers_left.remove(number)
            else:
                numbers_left.
