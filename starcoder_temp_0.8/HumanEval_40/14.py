

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
    # INSERT YOUR CODE HERE
    # HINT:
    #   You should be able to solve this in O(N^2) time,
    #   but you can do it in O(N log N) time.
    #   To do it in O(N log N), you should sort the list
    #   (and use a map to track duplicates), then use two pointers
    #   to iterate through the list.
    #   To do it in O(N^2), you should iterate through the list
    #   using one pointer and use another to iterate through the
    #   rest of the list.

