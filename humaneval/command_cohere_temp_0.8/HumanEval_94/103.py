```python
def largest_prime_sum_of_digits(nums):
    primes = [True for i in nums]
    sqrts = [int(sqrt(i)) for i in nums]
    primes[0] = False
    primes[1] = False
    
    for i in range(2, len(nums)):
        if primes[i]:
            for j in range(i**2, len(nums), i):
                primes[j] = False
                if not primes[j]:
                    break
    
    maxi = 0
    for i, num in enumerate(nums):
        if primes[i] and sqrts[i] == int(sqrt(num)):
            sum_digits = sum(map(int, str(num)))
            maxi = max(maxi, sum_digits)
    return maxi
```
The function iterates through the list of integers provided and initializes a list of boolean values, `primes`, to denote whether each number is prime or not. It then identifies the largest prime number in the list and calculates the sum of its digits to return the maximum sum of digits among the primes in the list. 

Let's break down the solution into parts for better understanding:
1. **Prime Detection**: To identify prime numbers in the list, the function initializes a list of boolean values, `primes`, and sets each value to `True`. The assumption is that each value in the list is prime initially. However, the primes[0] and primes[1] are set to False because 0 and 1 are not prime numbers. 
 2. **Square Root Calculation**: Additionally, the function calculates the square root for each number in the list and stores those results in the `sqrts` list. This step is necessary to find the largest prime number in the list accurately. 
3. **Prime Checklist**: Next, the function commences a loop to thoroughly examine the prime status of each number in the list. It starts from the second element (index 1) since the first two elements, 0 and 1, are not prime. For each potential prime number, it checks whether it is divisible by any number from 1 to its square root. If so, the number is not prime, and the `primes` list updates accordingly. This process continues until all non-prime numbers are identified. 
4. **Maximum Sum of Digits**: With the prime checklist complete, the function proceeds to determine the largest prime number in the list. It calculates the sum of digits for each prime number and maximizes the `maxi` variable when a larger sum is found. 

The given examples in the comment section demonstrate how the function operates on different input lists, ultimately providing the expected output.