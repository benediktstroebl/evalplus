def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w