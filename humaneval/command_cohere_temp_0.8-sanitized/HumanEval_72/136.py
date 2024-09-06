def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) // 2) and all(q[i] == q[~i] for i in range(len(q) // 2))