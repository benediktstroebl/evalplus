def will_it_fly(q, w):
    return (sum(q) <= w) and (w % 2 == 0) and all(q[i] == q[~i%len(q)] for i in range(len(q)))