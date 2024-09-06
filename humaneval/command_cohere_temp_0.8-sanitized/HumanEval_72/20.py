def will_it_fly(q, w):
    return (w >= sum(q)) and (w <= max(q)) and (q == q[::-1])