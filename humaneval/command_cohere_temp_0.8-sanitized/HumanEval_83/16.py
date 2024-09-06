def starts_one_ends(n):
    # Create a list to store the counts for starting and ending with 1
    counts = [0, 0]
    
    # Loop through numbers from 1 to n^2, handling cases of starting and ending with 1
    for num in range(1, n * n + 1):
        if num % 10 == 1:
            counts[0] += 1
        if num % 10 == 1 or num == num // 10 + 1:
            counts[1] += 1
    
    # Return the sum of the counts, as the answer is the total count divided by 2
    return sum(counts)