def double_the_difference(numbers): 
    odd_numbers = [num for num in numbers if num % 2 == 1]
    return sum(square(num) for num in odd_numbers) if odd_numbers else 0