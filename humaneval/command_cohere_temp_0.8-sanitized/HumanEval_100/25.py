def make_a_pile(n):
    # Get the next odd or even number
    def get_next_num(current):
        return current + 2 if current % 2 else current + 1
    
    # Generate the pile of stones
    pile = [n]
    while len(pile) < n + 1: 
        pile.append(get_next_num(pile[-1]))
    return pile