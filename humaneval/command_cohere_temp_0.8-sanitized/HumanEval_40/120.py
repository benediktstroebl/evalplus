def triples_sum_to_zero(lst):
    # Using Counter to count the number of items with certain values
    cnt = Counter(lst)
    # Filtering for the items that can be part of the trio with sum equal to 0
    possible_triples = [k for k, v in cnt.items() if v == 3 and k == -sum(set(lst) - {k})]
    return len(possible_triples) > 0