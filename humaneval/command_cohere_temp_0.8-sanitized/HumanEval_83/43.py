def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 9)
    
    # Iterate through potential starting digits from 1 to 9
    for start in range(1, 10):
        # Iterate through potential ending digits from 0 to n-1
        for end in range(0, n):
            # If the current potential number has a length of n
            if start + end + 1 == n:
                # Increment the count if the potential number starts or ends with 1
                if start == 1 or end == 0:
                    counts[end] += 1
    
    # Return the count of acceptable numbers
    return counts[-1]