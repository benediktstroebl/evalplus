def make_a_pile(n):
    # Get the next odd or even number
    def get_next_number(current):
        return current + 2 if current % 2 else current + 1

    # Generate the pile of stones
    pile = [n]
    for i in range(1, n + 1):
        pile.append(get_next_number(pile[i - 1]))

    return pile