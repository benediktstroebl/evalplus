def triples_sum_to_zero(lst):
    # Use Counter to count occurrences of elements in the list
    count = Counter(lst)

    # Test if any 3 elements sum up to zero
    for a in count:
        if count[a] > 2 and sum([a, -a, 0]) == 0:
            return True

    return False