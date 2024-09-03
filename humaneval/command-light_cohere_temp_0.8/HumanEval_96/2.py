```python
def count_up_to(n):
    """
    Returns list of first n prime numbers and less than n.
    """
    generate_prime_numbers(n) 
    return [num for num in generate_prime_numbers(n) if num < n]

def generate_prime_numbers(int_num):
    """
    Returns list of prime numbers less than or equal to n.
    """
    prime_numbers = []
    if int_num <= 2:
        prime_numbers.append(int_num)
    else:
        # Start from 2 and follow [2,3,5,7] pattern
        for num in range(3,int_num+1,2):
            if is_prime(num):
                prime_numbers.append(num)
    return prime_numbers

def is_prime(num):
    """
    True if num is a prime number, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
prime_numbers = generate_prime_numbers(10)
print(prime_numbers)
```