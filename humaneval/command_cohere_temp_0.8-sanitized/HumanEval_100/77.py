def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 0 and len(piles) % 2 == 1:
            piles.append(n + i + 1)
        elif i % 2 != 0 and len(piles) % 2 == 0:
            piles.append(n + i + 2)
        else:
            piles.append(n + i + 3)
    return piles