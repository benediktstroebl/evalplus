def triples_sum_to_zero(lst):
    # Write your code here. Read the emptylist as a signal to ignore this test
    if not lst:
        return False

    seen = set()
    for i, x in enumerate(lst):
        if x == 0:
            continue
        elif i > 1 and lst[i] == -lst[i - 2] - lst[i - 1]:
            return True
        elif i > 0 and lst[i] == -lst[i - 1] - x:
            return True
        elif x != 0 and (x, -x) not in seen:
            seen.add((x, -x))
            if lst.count(x) > 1 and lst.count(-x) > 1:
                return False
            if triples_sum_to_zero(lst[lst.index(x) + 1:]) or triples_sum_to_zero(lst[lst.index(-x) + 1:]):
                return True
    return False