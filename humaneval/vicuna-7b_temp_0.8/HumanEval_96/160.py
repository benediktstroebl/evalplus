
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
    prime_numbers = [2,3,5,7,11,13,17,19]
    nums = [i for i in range(1,n+1)]
    count = [0]*(n+1)
    for num in nums:
        if num in prime_numbers:
            count[num] = count[num] + 1
            for p in prime_numbers:
                if (p-num) in count:
                    count[p-num] = count[p-num] - 1
                    if count[p-num] == 0:
                        break
    return count.copy()
print(count_up_to(12))