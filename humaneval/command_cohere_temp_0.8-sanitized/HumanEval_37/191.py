def sort_even(l):
    even, odd = separate_ev(l)
    return combine_ev_od(odd, sorted(even))
def separate_ev(l):
    # separate list into even and odd indices
    # return two lists, even and odd
    even = [l[i] for i in range(0, len(l), 2)]
    odd = [l[i] for i in range(1, len(l), 2)]
    return even, odd
def combine_ev_od(o, e):
    # combine even indexed list with odd indexed list
    # return a single list combined
    return o + e