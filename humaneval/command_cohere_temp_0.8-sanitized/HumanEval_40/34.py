def triples_sum_to_zero(lst):
    # Split the list into chunks of three to efficiently check for triples
    # that sum up to zero.
    triples = [(lst[i:i+3]) for i in range(0, len(lst), 3)]
    
    # Iterate through the chunks and return True if a valid triple is found.
    for triple in triples:
        if sum(triple) == 0:
            return True
    
    return False