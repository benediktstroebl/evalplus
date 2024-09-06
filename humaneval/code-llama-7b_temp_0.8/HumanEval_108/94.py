
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
    def sum_digits(num):
        if num < 0:
            num *= -1
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    count = 0
    for i in range(len(arr)):
        num = arr[i]
        sum = sum_digits(num)
        if sum > 0:
            count += 1
    return count


