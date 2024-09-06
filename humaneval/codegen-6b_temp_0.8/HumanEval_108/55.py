
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
    # IF AN ELEMENT IS A NUMBER (INTEGER) THEN A SUM DIGIT IS IN THE
    # EACH DIGIT IS SUBSET OF THE AVERAGE OF EACH DIGIT IS
    # ODD OR EVEN FOR A NUMBER (INTEGER)
    # THEN CAN I SUM THE DIGITS FOR IT?
    # YES
    # NUMBERS LESS THAN -10 CAN'T HAVE THEIR SUM DIGITS
    # SUM DIGITS CAN BE AVERAGED
    # IF NOT, RETURN 0
    return sum(1 for num in arr if num > 0 and sum(digit for digit in str(num)) > 0)
