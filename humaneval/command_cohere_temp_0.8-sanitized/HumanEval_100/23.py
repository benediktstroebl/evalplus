def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 1:
            piles.append(i + 3)
        else:
            piles.append(i + 4)
    return piles