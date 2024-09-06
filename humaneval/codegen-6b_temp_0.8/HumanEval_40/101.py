

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # Your code here
    dict_of_numbers = {}
    counter = 0
    for number in l:
        if number not in dict_of_numbers:
            dict_of_numbers[number] = 1
        else:
            dict_of_numbers[number] += 1
    for number in l:
        if number in dict_of_numbers:
            if dict_of_numbers[number] == 3:
                counter += 1
            if counter == 3:
                return True
    return False

