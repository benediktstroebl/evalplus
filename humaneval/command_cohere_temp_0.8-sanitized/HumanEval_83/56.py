def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Calculate the count for starting with 1
    start_with_one = ((n - 1) * (n)) // 2
    counts = [start_with_one] + counts

    # Calculate the count for ending with 1
    end_with_one = ((n - 1) * n) // 2
    counts = counts + [end_with_one]

    # Sum up the counts to get the final result
    return sum(counts)