def triples_sum_to_zero(lst):
    # Use Counter to count occurrences of elements in the list
    cnt = Counter(lst)
    
    # Check if any two elements have a sum of the third distinct element
    for el1, el2 in cnt.items():
        if el1 + el2 == 0 and len(cnt) == 2:
            return True
    
    return False