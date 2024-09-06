

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

    # List that holds all possible sums of all elements in the list
    sum_list = []

    # Checks if there is at least 3 elements
    if len(l) < 3:
        return False

    # Adds all sums to sum_list
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            sum_list.append(l[i] + l[j])

    # Checks if there are any sums equal to 0
    return 0 in sum_list

    # or if you prefer the one-liner
    # return any(i == 0 for i in (sum(e) for e in combinations(l, 2)))

