def double_the_difference(numbers):
    odd_sum = 0
    non_integer = 0
    negative = 0
    for num in numbers:
        if type(num) == int:
            if num % 2 == 1:
                odd_sum += num
        else:
            negative += num
    return odd_sum + negative