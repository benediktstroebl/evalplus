def will_it_fly(q, w):
    return q[0] <= w and len(q) <= w
    q = [3, 2, 3]  # Example list
    w = 1  # Example weight

    return will_it_fly(q, w) == True