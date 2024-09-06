def cycpattern_check(a, b):
    a, b = a or '', b or ''
    for rotation_pos in range(len(b) // 2, -1, -1):
        if b[:rotation_pos] in a:
            return True
    return False