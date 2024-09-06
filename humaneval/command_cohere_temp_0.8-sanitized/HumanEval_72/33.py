def will_it_fly(q, w):
    return (len(q) == 1 or len(q) == 2 and q[0] == q[1]) and sum(q) <= w