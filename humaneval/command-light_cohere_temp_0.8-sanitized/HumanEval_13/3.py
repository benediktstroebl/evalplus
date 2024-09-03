def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a

    if a == b:
        return a
    
    # Write a loop that finds the largest divisor of a and b
    return max(a, b)