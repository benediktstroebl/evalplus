def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)