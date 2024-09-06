

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

    seen = {}
    for i in l:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

    seen_set = set(seen.keys())
    for i in seen_set:
        if seen[i] > 2:
            return False

    # adding first element twice
    new_l = [l[0]]
    for i in l[1:]:
        new_l.append(i)
        new_l.append(i)

    new_l.sort()

    # O(n) runtime
    i = 0
    j = len(new_l) - 1
    while i < j:
        sum = new_l[i] + new_l[j]
        if sum == 0:
            return True
        elif sum < 0:
            i += 1
        elif sum > 0:
            j -= 1
    return False

