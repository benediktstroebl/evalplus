def make_a_pile(n):
    # Determines the next level accordingly based on the parity of n.
    # If n is even, it takes the next even number, else the next odd number.
    level = [n]
    if n % 2 == 0:
        while n % 2 == 0:
            n += 2
    else:
        while n % 2 != 0:
            n += 1
    return level + [n]