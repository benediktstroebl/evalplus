```python
def is_multiply_prime(a):
    prime_factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
``` 

The code defines a Python function called `is_multiply_prime` that checks whether a given number `a` is the product of exactly three prime factors. It iterates through factors from 2 up to the square root of `a`, and progressively divides `a` by each prime factor it finds. The function returns True if the number can be divided exactly three times without leaving a remainder, indicating that it's the product of three distinct prime factors, and False otherwise.

Here is a markdown code block with corresponding tests to verify the correctness of the solution:
```python
# Testing the is_multiply_prime function
a = 30
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 49
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 36
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 27
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 25
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 9
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")
```

The code then prints the result of the function for numbers from the example as well as additional numbers to demonstrate the function's behavior for different cases. 

The full code after the execution of the corresponding tests will look as follows: 
```python
# Testing the is_multiply_prime function
a = 30
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 49
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 36
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 27
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 25
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

a = 9
print(f"{a} == is_multiply_prime(a): {is_multiply_prime(a)}")

``` 

The first test illustrates that the function `is_multiply_prime` appropriately identifies true for numbers that are the result of multiplying three prime numbers, whereas the last test case demonstrates that the function recognizes the correct false outcome for a number that is not the product of precisely three prime factors.