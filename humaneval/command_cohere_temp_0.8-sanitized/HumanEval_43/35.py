def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            complement = -i
        else:
            complement = i
        if complement in seen:
            return True
        seen.add(i)
    return False