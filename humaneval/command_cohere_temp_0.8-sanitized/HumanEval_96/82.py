def count_up_to(n):
    # Create a list to store the prime numbers up to n.
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = []
    current_num = 2
    while len(result) < n and current_num < n:
        if current_num in prime_numbers:
            result.append(current_num)
        elif current_num < n and current_num % prime_numbers[0] != 0 and current_num % prime_numbers[1] != 0:
            # Skip non-prime numbers and check the next number
            current_num += 1
        else:
            current_num += 1
    return result