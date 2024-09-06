
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
    count_arr = []
    prime_nums = [2, 3]
    while len(count_arr) < n:
        current_num = prime_nums[0]
        while prime_nums[0] < n:
            if check_if_prime(current_num):
                prime_nums.append(current_num)
            current_num += 1
        count_arr.append(current_num)
    return count_arr

