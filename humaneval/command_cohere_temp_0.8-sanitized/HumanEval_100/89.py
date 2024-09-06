def make_a_pile(n):
    # Get the next odd or even number based on the parity of n
    def get_next_parity_number(parity):
        return 2 * (parity - 1) + 1 if parity else 2

    # Generate the list of stone counts
    stone_counts = [n]
    for i in range(1, n.bit_length() + 1):
        stone_counts.append(get_next_parity_number(stone_counts[i] & 1))

    return stone_counts