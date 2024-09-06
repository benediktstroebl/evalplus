def unique_digits(x):
    odd = [elem for elem in x if not any(int(c) % 2 == 0 for c in str(elem))]
    return sorted(odd)