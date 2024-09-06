def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # alternatively, you can use this simpler condition (a bit less efficient):
    # return (len(q) == 1) or (sum(q) <= w < len(q) // 2)