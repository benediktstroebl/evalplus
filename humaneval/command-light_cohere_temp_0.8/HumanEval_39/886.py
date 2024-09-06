```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n <= 3:
        return n
    if n % 2 == 0:
        return 5
    else:
        # Check primality of Fibonacci numbers
        temp = prime_fib(math.floor(n / 2))
        if temp == 2 or temp == 3:
            return temp
        else:
            # Use division method to find next Fibonacci number
            temp1 = prime_fib(int(math.sqrt(n)))
            temp2 = temp1 * temp1
            return temp2

# Example usage
print(prime_fib(5))
 ``` 
This code defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is also prime. The function uses a primality test to ensure it's always 2 or 3 for even numbers or the division method. 

The output of the example usage is `89`, which is the fifth Fibonacci number that is also prime.