def triples_sum_to_zero(lst):
    # Using sorting to simplify the task
    lst.sort()
    for i in range(len(lst) - 2):
        if lst[i] + lst[i + 1] + lst[i + 2] == 0:
            return True
    return False