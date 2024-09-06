def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations of size 3
    # in the list. Using len({...}) == 1 catches the case when there is
    # exactly one sum that is possible to form with 3 elements, but this
    # is not the sum that we want (sum == 0 in this case).
    if len(set(sum_combinations_to_zero(lst, 3))) == 1 and lst:
        return False
    else:
        return True
def sum_combinations_to_zero(lst, n):
    # Using Counter to find sums of different lengths.
    # Using the exponentiation by squaring pattern to make the nested loop
    # less expensive in terms of number of sums tried.
    counter = Counter(lst)
    if n == 1:
        return list(counter.keys())
    return [x for x in sum_combinations_to_zero(counter, n // 2)
            if any(y in counter and x - y in counter and z in counter
                    and x - y + z == 0 for z in counter for y in counter)]