def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or q == [] or q == [q[0] + q[-1]] or q == [q[0]-q[-1], q[0]])