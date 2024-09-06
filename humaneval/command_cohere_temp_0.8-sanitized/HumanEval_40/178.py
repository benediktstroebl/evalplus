def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    counter = Counter(lst)
    
    # Filtering elements that can form a sum of zero with another element in the list
    candidates = [k for k, v in counter.items() if v > 1 and k != 0]
    
    # Checking if there are exactly two candidates and they form a pair that sums up to zero
    return len(candidates) == 2 and (sum(candidates) + counter[0]) == 0