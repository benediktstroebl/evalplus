
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
    count = 0
    nums = []
    # create a list of integers s.t 1<=s<=n
    for i in range(1, n+1):
        nums.append(i)
    # remove all multiples of 2
    nums = [i for i in nums if i % 2 != 0]
    # remove all multiples of 3,5,7,11,13,17
    for i in nums:
        if i % 3 == 0:
            nums.remove(i)
        elif i % 5 == 0:
            nums.remove(i)
        elif i % 7 == 0:
            nums.remove(i)
        elif i % 11 == 0:
            nums.remove(i)
        elif i % 13 == 0:
            nums.remove(i)
        elif i % 17 == 0:
            nums.remove(i)
    # add all prime numbers as integers to count
    count = count + nums
    return count
