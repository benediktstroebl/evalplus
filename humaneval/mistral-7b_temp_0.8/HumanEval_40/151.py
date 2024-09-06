

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
    # your code here
    # return True if there are 3 numbers in the list that sum to 0
    # else return False

    # time complexity: O(n^3)

    # we go through each element in the array, compare it to every other
    # element in the array, then compare it to every other element in
    # the array
    # so, we are doing n^3 iterations

    # space complexity: O(1)

    # we are only using one variable, the index variable, so we are using
    # constant space
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue
            for k in range(len(l)):
                if i == j or i == k or j == k:
                    continue
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
