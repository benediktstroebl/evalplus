def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Calculate the count for starting with 1
    start_with_one = ((n - 1) // 2) * 2
    counts += [start_with_one] * n

    # Calculate the count for ending with 1
    if n % 2 == 0:
        end_with_one = n // 2
        counts += [end_with_one] * (n - 1)
    else:
        end_with_one = (n - 1) // 2
        counts += [end_with_one]

    # Return the total count
    return sum(counts)