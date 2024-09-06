def triples_sum_to_zero(lst):
    # Split the list into consecutive pairs
    consecutive_pairs = list(zip(lst, lst[1:]))
    # Filter out pairs that sum to zero
    filtered_pairs = [pair for pair in consecutive_pairs if sum(pair) == 0]
    # Check if there are exactly three elements in the list
    return len(filtered_pairs) == 3