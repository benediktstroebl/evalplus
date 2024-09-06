
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
    # Your code here

    def digits(number):
        if number == 0:
            return [0]
        else:
            return digits(number // 10) + [number % 10]
    
    def first_digit(number):
        return abs(digits(number)[0])
    
    def is_negative(number):
        return number < 0

    total_nums = 0
    
    for number in arr:
        # print(number, digits(number), first_digit(number), is_negative(number))
        # print(digits(number), first_digit(number), is_negative(number))
        
        if is_negative(number) == False:
            sum_of_digits = 0
            for digit in digits(number):
                sum_of_digits = sum_of_digits + digit
            if sum_of_digits > 0:
                total_nums = total_nums + 1
        else:
            sum_of_digits = 0
            for digit in digits(number):
                sum_of_digits = sum_of_digits + digit
            if sum_of_digits > 0:
                total_nums = total_nums + 1
    return total_nums


