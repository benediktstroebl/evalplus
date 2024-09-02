

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
    # find all unique pairs
    # compare to remaining elements

    pairs = set()
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         pairs.add((l[i], l[j]))

    # unique_pairs = []
    # for pair in pairs:
    #     if pair not in unique_pairs:
    #         unique_pairs.append(pair)

    # pairs = []
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if (l[i], l[j]) not in pairs:
    #             pairs.append((l[i], l[j]))

    # unique_pairs = []
    # for pair in pairs:
    #     if pair not in unique_pairs:
    #         unique_pairs.append(pair)

    # pairs = [(l[i], l[j]) for i in range(len(l)) for j in range(i+1, len(l))]
    # unique_pairs = list(set(pairs))
    # print(pairs, unique_pairs)

    pairs = set()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            pair = (l[i], l[j])
            if pair not in pairs:
                pairs.add(pair)

    # print(pairs, unique_pairs)
    unique_pairs = list(pairs)
    for pair in unique_pairs:
        if -pair[0] in l and -pair[1] in l:
            return True

    return False

