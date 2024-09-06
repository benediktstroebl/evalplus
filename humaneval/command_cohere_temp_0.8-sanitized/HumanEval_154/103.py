def cycpattern_check(a, b):
    s = set()
    s.add(a)
    s.add(b)
    s.add(b + b)
    s.add(b + b + b)
    return b in s.intersection(set(a))
    # Your code here!