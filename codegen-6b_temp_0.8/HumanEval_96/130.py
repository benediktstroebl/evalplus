
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
    # Code a function that takes an non-negative integer n and returns a list containing the prime number
    # less than n.
    # Hint: You should use a for loop and count_up_to_prime(n)
    def count_up_to_prime(n):
        if n == 1:
            return []
        elif n == 2:
            return [2]
        else:
            prime_list = [2]
            for i in range(3, n + 1, 2):
                for j in range(len(prime_list)):
                    if i % prime_list[j] == 0:
                        break
                else:
                    prime_list.append(i)
            return prime_list
    return count_up_to_prime(n)

