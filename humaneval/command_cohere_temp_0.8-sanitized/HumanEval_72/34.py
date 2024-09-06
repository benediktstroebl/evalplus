def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # reverse = list(reversed(q))  # primer pyazi pytus
    # return (sum(q) <= w) and (w <= len(q) == len(set(q)) == len(set(reverse)) )