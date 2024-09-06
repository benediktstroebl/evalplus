def count_up_to(n):
    # check if n is 0 or 1, if so, return an empty list
    if n < 2:
        return []
    # Create a list to store the first n prime numbers less than n
    count_up = []
    # Start from the first prime number (2) and loop until n is divisible by 2 or reached
    for i in range(2, int(n**0.5) + 1):
        # if n is divisible by i add i to count up and check if n is divisible by i or not
        if n % i == 0:
            count_up.append(i)
            if i >= n // 2:
                break
    # Return the count up list
    return count_up