def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations of size 3
    # where the remainder of the difference of the sum and the product
    # is either 0 or 2 to avoid even or odd sums
    counter = Counter(lst)
    for x, y in counter.items():
        if y % 2 == 0 or y % 3 == 0:
            counter[x] = 0
    for x, y in counter.items():
        if counter[x] == 2 and x + y + counter[x + y] == 0:
            return True
    return False