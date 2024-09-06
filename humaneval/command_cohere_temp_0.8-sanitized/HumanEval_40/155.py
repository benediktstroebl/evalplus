def triples_sum_to_zero(lst):
    # Define the 3-tuple cache
    trios = {}
    
    # Initialize the count of qualifying trios
    count = 0
    
    # Examine each trio of elements in the list
    for a, b, c in itertools.combinations(lst, r=3):
        # Calculate the sum of the trio
        sum_ = a + b + c
        
        # Check if the sum is zero and the trio is unique
        if sum_ == 0 and (a, b, c) in trios:
            count += 1
        trios[(a, b, c)] = True
    
    # Return the count of qualifying trios
    return count > 0