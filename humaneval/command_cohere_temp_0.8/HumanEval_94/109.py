```python
def largest_prime_sum_of_digits(nums):
    """Return the largest prime sum of digits for a list of integers."""
    nums.sort()
    largest_prime = nums[0]
    for num in nums:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                if num > largest_prime:
                    largest_prime = num
    return sum(map(int, str(largest_prime)))
```

The function `largest_prime_sum_of_digits` iterates through the list of integers, sorting them in ascending order. For each number greater than 1, it checks for primality by iterating through a range that starts from 2 and ends at the square root of the number (`int(num**0.5) + 1`). If the number is prime, it compares it to the current `largest_prime`, updating it if the new prime is larger. Finally, the sum of the digits of the largest prime is calculated by converting it to a string and mapping each character to an integer. The resulting sum is returned as the output. 

This approach efficiently finds the largest prime number within the list and calculates the sum of its digits.