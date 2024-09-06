def cycpattern_check(a, b):
    a = a.lower()
    b = b.lower()
    b = b.strip('.,!?()[]{}')
    return (b in a or a.startswith(b) or a.endswith(b) or b in a[1:])