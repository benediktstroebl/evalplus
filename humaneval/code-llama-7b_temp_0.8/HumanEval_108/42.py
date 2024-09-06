
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    "*** YOUR CODE HERE ***"
    # for i in range(len(arr)):
    #     count = 0
    #     negative = False
    #     for j in range(len(str(abs(arr[i])))):
    #         if int(str(abs(arr[i]))[j]) > 0:
    #             count += 1
    #         if int(str(abs(arr[i]))[j]) < 0:
    #             negative = True
    #     if negative == True:
    #         count -= 1
    #     if negative == False:
    #         count += 1
    #     if count > 0:
    #         return count
    # return 0

    sum_of_digits = lambda num: sum([int(c) for c in str(abs(num))])
    return sum([1 for n in arr if sum_of_digits(n) > 0])


