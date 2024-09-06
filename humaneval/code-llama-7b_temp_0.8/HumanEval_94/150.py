

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

    import math

    max_prime_number = -1
    lst_of_prime_numbers = []

    for number in lst:
        if number >= max_prime_number:
            for i in range(number + 1):
                for j in range(number + 1):
                    if i != j:
                        if i * j == number:
                            if i != 0:
                                if j != 0:
                                    lst_of_prime_numbers.append(number)

    new_lst = [0] * len(lst_of_prime_numbers)
    for i in range(len(lst_of_prime_numbers)):
        new_lst[i] = int(str(lst_of_prime_numbers[i]))

    for i in range(len(new_lst)):
        max_prime_number = new_lst[i]
        if max_prime_number >= max_prime_number:
            for i in range(max_prime_number + 1):
                for j in range(max_prime_number + 1):
                    if i != j:
                        if i * j == max_prime_number:
                            if i != 0:
                                if j != 0:
                                    new_lst[i] = new_lst[j]

    sum_of_digits = 0
    for i in range(len(new_lst)):
        sum_of_digits += math.log10(new_lst[i])

    return int(sum_of_digits)


