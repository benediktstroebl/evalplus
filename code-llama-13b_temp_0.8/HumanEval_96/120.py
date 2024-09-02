
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

    if n < 2:
        return []
    nums = [1] * n
    nums[0] = 0
    nums[1] = 0
    nums_count = 0

    for i in range(2, n):
        if nums[i] != 0:
            for j in range(2, n // i):
                nums[i * j] = 0

    return [i for i in range(2, n) if nums[i] != 0]
