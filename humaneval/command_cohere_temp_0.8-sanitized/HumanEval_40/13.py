def triples_sum_to_zero(lst):
    # Define possible triple combinations and initialize count and product to zero
    combinations = [(x, y, -(x + y)) for x, y in combinations(lst, 2)]
    count = 0
    product = 1
    # Sort combinations by smallest sum
    combinations = sorted(combinations, key=lambda x: x[2])
    # Check if any combination sums to zero
    for x, y, z in combinations:
        if z == 0:
            count += 1
            product *= x * y
    return product if count == 1 else False