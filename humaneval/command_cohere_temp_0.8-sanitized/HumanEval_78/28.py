import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0

    # check if the number is an empty string or a hexadecimal number
    if re.match(r'^[0-9A-F]+$', num) and num:
        # convert hexadecimal string to an integer to simplify the rest of the algorithm
        num = int(num, 16)

        while num > 0:
            # divide the number by 2 to find the prime numbers
            num //= 2
            prime_count += (num & 1)

            # add the prime numbers found to the list of primes
            for i in range(0, len(primes)):
                if num == primes[i]:
                    prime_count += 1
                    break

            # remove the prime numbers from the list of primes to avoid counting them twice (or more)
            for i in range(0, len(primes)):
                if primes[i] == str(num):
                    primes.remove(primes[i])
                    break

        # count the number of prime hexadecimal digits
        for digit in hex_digits:
            if digit in primes:
                prime_count += 1

    return prime_count