def will_it_fly(q, w):
    return (sum(q) <= w) and palindromic_list(q)
def palindromic_list(l):
    return l == l[::-1]