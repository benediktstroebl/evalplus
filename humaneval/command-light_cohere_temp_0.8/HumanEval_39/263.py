```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # Finding all prime factors and constructing Fibonacci number using those factors
        prime_factors = []
        for i in range(5, n + 1, 5):
            is_prime = True
            for j in range(2, int(i**0.5) + 1,  :
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_factors.append(i)
        fibonacci = 1
            for prime in prime_factors:
                fibonacci *= prime
            return fibonacci
``` 
The provided code is a Python script that defines a function called prime_fib. It takes an iterative approach to generate the n-th Fibonacci number that is prime. 

The function begins by checking if the number is less than or equal to 1, in which case it returns the number itself. If the number is greater than 3, the function returns 3, indicating that Fibonacci numbers of size greater than 3 are composite and not prime. 

The function then iterates through numbers from 5 to n, checking each number for primality. It keeps track of prime factors using a list and constructs the Fibonacci number using these prime factors. 

Finally, the function returns the generated Fibonacci number.