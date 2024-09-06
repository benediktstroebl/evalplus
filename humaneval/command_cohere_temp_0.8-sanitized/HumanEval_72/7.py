def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # alternatively, you could use this formulation:
    # return (sum(q) <= w) and all(q.count(i) % 2 == 0 for i in set(q))