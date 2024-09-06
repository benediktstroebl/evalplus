def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    
    rotations = [second, second[1:] + second[:1], second[2:] + second[:2]]
    
    return any(second in first for second in rotations)