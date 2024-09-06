def make_a_pile(n):
    # Get the next odd or even number based on the input being odd or even
    def get_next_number(input_num):
        return (input_num + 1) if input_num % 2 else (input_num + 2)
    
    # Generate the pile of stones
    pile = [n]
    while len(pile) < n + 1:
        pile.append(get_next_number(len(pile) % 2))
    
    return pile