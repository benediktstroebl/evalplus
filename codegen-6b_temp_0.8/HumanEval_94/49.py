

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    prime_list = []
    for i in lst:
        run = True
        for j in range(2, i-1):
            if i % j == 0:
                run = False
        if run:
            prime_list.append(i)
    biggest = max(prime_list)
    big_len = len(str(biggest))
    cur_sum = sum([int(i) for i in list(str(biggest))])
    for i in range(big_len-1):
        for j in range(i+1, big_len):
            test_sum = sum([int(k) for k in list(str(biggest) + str(big_len-j))])
            if test_sum > cur_sum:
                cur_sum = test_sum
    return cur_sum

