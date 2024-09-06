def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    counter = Counter(lst)
    
    # Filtering elements that have a sum of zero when combined with their reciprocal
    candidates = [x for x in counter if x + 1 / x == 0]
    
    # Checking if there are exactly three distinct elements that satisfy the condition
    return len(candidates) == 3