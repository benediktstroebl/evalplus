def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations and perform sums
    # Counter provides a quick solution to the problem by taking unique values from the list and returning all possible combinations of three elements.
    # Then it performs summation on each combination and returns True if a combination results in sum 0
    return any(sum(combination) == 0 for combination in Counter(lst).combinations(3))