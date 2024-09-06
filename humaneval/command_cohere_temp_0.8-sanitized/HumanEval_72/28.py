def will_it_fly(q, w):
    return (len(q) == 1 or len(set(q)) == len(q)) and sum(q) <= w