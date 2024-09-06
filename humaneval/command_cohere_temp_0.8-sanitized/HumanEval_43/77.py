def pairs_sum_to_zero(l):
    # Go through each element and find its pair
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False