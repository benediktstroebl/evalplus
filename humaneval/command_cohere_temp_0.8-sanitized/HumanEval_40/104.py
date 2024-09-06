def triples_sum_to_zero(lst):
    # Use Counter to count occurrences of elements in the list
    counts = Counter(lst)
    
    # Test if any (a, b, -a-b) triple exists
    return any(v >= 3 for a, b in counts.items() if b >= 2 and -(a + b) in counts)