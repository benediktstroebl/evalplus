def will_it_fly(q, w):
    return (sum(q) <= w) and palindromic_list(q)
def palindromic_list(q):
    if len(q) == 1:
        return True
    else:
        if q[0] == q[-1]:
            return palindromic_list(q[1:-1])
        else:
            return False