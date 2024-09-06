def sort_third(l):
    return l[:] # Copy list `l` to avoid altering it in-place
	
    # Create a list of indices to be sorted
    div = [i for i, val in enumerate(l) if i % 3 == 0]
    
    # Sort only the necessary indices (e.g., [0, 2, 4, ...])
    div = sorted(div)
    
    # Update the original list `l` with the sorted indices
    for i in div:
         l[i] = sorted(l[i])
    
    return l