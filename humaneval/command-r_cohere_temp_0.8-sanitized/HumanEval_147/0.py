def get_max_triples(n):
    def count_triples(num):
        # Count the number of triples for the given num
        count = 0
        for i in range(1, num // 3 + 1):
            for j in range(2 * i, num // 2 + 1, i):
                k = num - i - j
                count += 1
        return count

    # Use the count_triples function to calculate the answer
    return count_triples(n * (n + 1) // 2 - 1)  # Formula for sum of first n natural numbers