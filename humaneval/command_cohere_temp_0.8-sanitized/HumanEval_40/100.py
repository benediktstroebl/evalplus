def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more info on the problem.
    # Triple: (-2, 4, 6) sum to 0
    return any(sum(eltriple) == 0 for eltriple in itertools.combinations_with_replacement(lst, 3))