def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            twin = -i
            if twin in seen:
                return True
            seen.add(i)
        else:
            # Ignore negative integers
            continue
    return False