def will_it_fly(q, w):
    return (sum(q) <= w) and (w <= len(q) == len(set(q)))
    # reverse to check for palindromic, set to check for unique
    # if both conditions are met, function returns true