def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            twice_i = 2 * i
            if twice_i in seen:
                return True
            seen.add(i)
        else:
            neg_i = -i
            if neg_i in seen:
                return True
            seen.add(i)
    return False