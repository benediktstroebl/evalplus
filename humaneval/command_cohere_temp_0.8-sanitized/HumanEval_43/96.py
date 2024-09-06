def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            num = -i
        else:
            num = i
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False