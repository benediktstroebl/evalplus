def triples_sum_to_zero(lst):
    # Use a hashmap to track sums of elements
    sums = {}
    for ele in lst:
        if ele not in sums:
            sums[ele] = 0
        sums[ele] += ele

    # Use sets to find distinct elements that sum to zero
    zero_triples = set()
    for x,xs in sums.items():
        if xs == 0:
            for y,ys in sums.items():
                if x + y == 0 and x != y:
                    zero_triples.add((x, y, xs))
                    zero_triples.add((x, xs, y))
                    zero_triples.add((xs, x, y))
                    zero_triples.add((xs, y, x))
    return len(zero_triples) > 0