def sort_third(l):
    return l[:1:-1] if len(l) % 3 == 0 else l[1::1][:len(l) - 1:-1]