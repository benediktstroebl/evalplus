def make_a_pile(n):
    # Get the next odd or even number based on the input being odd or even
    def get_next_number(input_num):
        if input_num % 2 == 0:
            return input_num + 2
        else:
            return input_num + 1
    # Generate the list of stone counts
    counts = [n]
    while len(counts) < n:
        if n % 2 == 1:
            n = get_next_number(n)
        else:
            n = get_next_number(n)
        counts.append(n)
    return counts