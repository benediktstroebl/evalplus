def double_the_difference(numbers):
    if not_list(numbers):
        return 0
    
    odd_numbers = [n for n in numbers if n % 2 == 1]
    result = sum([x ** 2 for x in odd_numbers if x >= 0])
    return result