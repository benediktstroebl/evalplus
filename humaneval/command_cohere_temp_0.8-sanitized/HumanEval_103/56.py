def rounded_avg(n, m):
    if n > m:
        return -1
    # Calculate the average
    total = (n + m) // 2
    count = m - n + 1
    average = total / count
    # Round the average to the nearest integer
    rounded_avg = round(average)
    # Convert to binary
    binary_representation = bin(rounded_avg)[2:]
    if binary_representation.startswith('0'):
        binary_representation = '0b' + binary_representation
    return binary_representation