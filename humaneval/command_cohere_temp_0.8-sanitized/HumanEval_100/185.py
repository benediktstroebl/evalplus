def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 0:
            piles.append(i + 2)
        else:
            piles.append(i + 1)
    return piles