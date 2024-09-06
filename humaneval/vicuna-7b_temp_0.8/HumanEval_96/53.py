
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    count = [1]
    prime_numbers = [2]
    while len(count) < n:
        for num in range(2, int(n**0.5) + 1):
            if num not in count:
                for p in prime_numbers:
                    if num % p == 0:
                        break
                    count.append(num)
        prime_numbers.append(num)
    return count

print(count_up_to(10))