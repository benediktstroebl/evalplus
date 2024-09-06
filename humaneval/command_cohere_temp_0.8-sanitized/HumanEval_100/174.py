def make_a_pile(n):
    piles = [n]
    while len(piles) < n + 1:
        if piles[-1] % 2 == 1:
            piles.append(piles[-1] + 2)
        else:
            piles.append(piles[-1] + 1)
    return piles