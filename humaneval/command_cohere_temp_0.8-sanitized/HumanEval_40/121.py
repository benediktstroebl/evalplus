def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    counter = Counter(lst)
    
    # Filtering elements that can form a sum of zero with another element in the list
    candidates = [x for x in counter if counter[x] >= 2 and x == -counter[x]]
    
    # Checking if there are exactly two candidates left and one of them is -x
    return len(candidates) == 2 and (-x in candidates for x in candidates if x != -x)