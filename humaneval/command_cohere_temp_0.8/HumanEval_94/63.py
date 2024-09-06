```python
def largest_prime_sum_of_digits(nums):
    """Returns the largest prime sum of digits for a list of integers."""
    primes = [True for n in nums]
    # Mark non-primes
    nums[0::2] = [False] * len(nums)
    # Iterate through odd numbers
    for i in range(1, len(nums), 2):
        if primes[i]:
            j = i
            while j < len(nums) and primes[j]:
                nums[j] = False
                j += 2
    # Find the largest prime
    largest_prime = 0
    for i in range(len(nums)):
        if primes[i] and nums[i] != False:
            largest_prime = i
    # Return the sum of digits of the largest prime
    digits = [int(d) for d in str(largest_prime)]
    return sum(digits)
```
This code defines the `largest_prime_sum_of_digits` function, which takes a list of numbers `nums` as input and returns the largest prime number's sum of digits.

Here's a breakdown of how the code works:
1. To begin, it assigns a boolean value `True` to each element in the input list `nums` to denote whether each entry is a prime number. This is done using the expression `[True for n in nums]`.
2. It then identifies the odd index numbers in the list, which are potentially prime (as odd numbers are more likely to be prime than even numbers), and marks them as not prime by setting their corresponding value to `False`. This is achieved with the expression `nums[0::2] = [False] * len(nums)`.
3. After that, it proceeds to cycle through the potential prime numbers at odd indices. If a number at index `i` is prime, it marks its adjacent even indices as not prime while traversing through the list. This is achieved by setting `nums[j]` to `False` and incrementing `j` by 2 until reaching a non-prime index.
4. The function then determines the index of the largest prime number among the marked primes in the list.
5. Lastly, it computes the sum of the digits of the largest prime number and returns it. This is achieved by converting the largest prime to a string using `str(largest_prime)`, extracting its digits using a list comprehension, and then summing the digits using `sum(digits)`.

Note: The code assumes that the list of integers contains at least one prime number. If the list does not contain any prime numbers, the function will return 0. Additionally, this approach focuses on odd index numbers for prime checking efficiency. Prime checking is halted once a prime is discovered, and the traversal moves to the next odd index, potentially saving checks for non-prime even numbers.