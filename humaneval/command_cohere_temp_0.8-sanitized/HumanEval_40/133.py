def triples_sum_to_zero(lst):
    # Using Counter to count the sum of distinct elements in the list
    # using itertools to check for triplets that sum to zero
    from collections import Counter
    from itertools import combinations

    # Count the sum of distinct elements in the list
    counter = Counter(lst)
    zero_sum_triplets = 0
    # Generate all unique size 3 combinations of the list and check if their sum is zero
    for el_comb in combinations(lst, 3):
        if sum(el_comb) == 0 and counter[sum(el_comb)] == 3:
            zero_sum_triplets += 1

    return zero_sum_triplets > 0