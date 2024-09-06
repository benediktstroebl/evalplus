
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
    # 先找到下一个素数
    def next_prime(num):
        while True:
            if is_prime(num):
                return num
            num += 1

    # 然后计算出范围内的素数列表
    if n <= 0:
        return []
    elif n == 1:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [2, 3]
    else:
        prime_list = []
        current_prime = 2
        while len(prime_list) < n:
            if current_prime >= n:
                break
            prime_list.append(current_prime)
            current_prime = next_prime(current_prime)
        return prime_list

