def triples_sum_to_zero(lst):
    # Write your code here. Read the docstring of the original function for more guidance.
    return any(el >= 0 for el in lst for x, y, z in combinations(lst, 3) if x + y + z == 0)