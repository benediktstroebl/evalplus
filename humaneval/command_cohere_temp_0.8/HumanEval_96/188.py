Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
# Markdown code block showing the implementation of the function 'count_up_to'
def count_up_to(n):
    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        # Check if the number is prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
        num += 1
    return prime_numbers
```
The function 'count_up_to' uses a simple method to find prime numbers and stores them in a list until the list has a length of 'n'. The function successfully handles the edge cases like 'count_up_to(0)', 'count_up_to(1)', and returns the correct prime numbers for the given 'n' values provided in the example.