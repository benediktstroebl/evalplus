def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations of size 3
    # where the remainder of the difference of the sum and zero is guaranteed
    # to be the difference between two of the elements
    counter = Counter(lst)
    for x, y in counter.items():
        if y % 2 == 1 and x == y - x:
            return True
    return False