

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

    # First sort the list
    l = sorted(l)

    # Define indices
    i = 0
    j = len(l) - 1

    # Run loop until index of first element reaches index of last element
    while i < j:

        # Calculate sum of three elements
        sum = l[i] + l[j] + l[j - 1]

        # If sum is equal to zero, return True
        if sum == 0:
            return True

        # Increment index of first element if sum is greater than zero
        if sum > 0:
            i += 1

        # Decrement index of last element if sum is less than zero
        if sum < 0:
            j -= 1

    # Return False if no three elements sum up to zero
    return False
