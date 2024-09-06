def sort_even(l):
    even, odd = separate_evens(l)
    return combine_evensort(even, odd)
def separate_evens(l):
    even, odd = [], []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd
def combine_evensort(even, odd):
    return [x for x in even] + [x for x in sorted(even)] + [x for x in odd]