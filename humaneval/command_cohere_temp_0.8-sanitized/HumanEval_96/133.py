def count_up_to(n):
    # check if n is 0 or 1, in that case return an empty list
    if n < 2:
        return []
    # initialize a list to store the prime numbers and an iterator
    prime_list = []
    num = 2
    while len(prime_list) < n:
        # iterate through integers until the list is complete or the passed integer is greater than n
        if num > n:
            break
        # iterate through integers 2, 3, 4, ..., n:
        for i in range(2, num):
            # Check if the number i is prime:
            is_prime = True
            for j in range(2, int(num**(0.5)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(i)
        num += 1
    return prime_list