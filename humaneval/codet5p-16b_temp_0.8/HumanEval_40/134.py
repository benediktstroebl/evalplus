

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

    count = 0

    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if (l[i] + l[j] + l[k]) == 0:
                    count += 1
                    print(f"{l[i]}, {l[j]}, {l[k]}")
    if count == 0:
        print(f"No triples sum to zero in list {l}")
    else:
        print(f"Triples sum to zero in list {l}")

