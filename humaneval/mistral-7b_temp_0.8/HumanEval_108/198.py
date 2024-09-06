
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
    # your code here
    if arr == []:
        return 0
    else:
        negatives = []
        count = 0
        for number in arr:
            total = 0
            number = abs(number)
            while number:
                digit = number % 10
                total += digit
                number = number // 10
            if total == 0:
                negatives.append(number)
            else:
                count += 1
        return count
        return len(negatives)

