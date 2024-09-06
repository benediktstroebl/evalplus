def triples_sum_to_zero(lst):
    # Split the list into triples
    tests = [(lst[i:i + 3]) for i in range(0, len(lst), 3)]
    
    # Check if any of the triples have a sum of zero
    return any(sum(x) == 0 for x in tests)