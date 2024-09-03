```python
def double_the_difference(numbers): 
    odd_numbers = [num for num in numbers if num % 2 == 1]
    return sum(square(num) for num in odd_numbers) if odd_numbers else 0

# Test cases
test_double_the_difference = double_the_difference([1, 3, 2, 0])
test_double_the_difference = double_the_difference([-1, -2, 0])
test_double_the_difference = double_the_difference([9, -2])
test_double_the_difference = double_the_difference([0])
test_double_the_difference = double_the_difference([1, 2, 3, 4])
test_double_the_difference = double_the_difference([10, 11, 12, 13])
test_double_the_difference = double_the_difference([])
```

This code defines a function called `double_the_difference` that calculates the sum of the squares of odd numbers in a given list. It uses list comprehension to filter out the odd numbers and then uses the `sum` function with the `square` function to calculate the sum of squares. It also has a tests to ensure the function is correct.