def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting digits (10...,
    # 100..., 1000...) and ending digits (1..., 11..., 101..., 111...)
    counts = [0, 1, 2, 3, 4, 6, 4, 6, 4, 6, 1]

    return counts[n - 1] if n <= 10 else sum(counts[i - 1] for i in range(n, 0, -1))