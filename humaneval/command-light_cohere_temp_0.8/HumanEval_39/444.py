```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    temp = prime_fib(n // 2)
    if temp == 2 or temp == 3:
        return temp
    return prime_fib(n)

# Example usage
print(prime_fib(5))
``` 
This function uses a simple recursive approach to find the n-th Fibonacci number that is prime, as well as checks for divisibility by 2 and 3 to quickly exit the recursion and avoid unnecessary calculations. The function then uses the infinite recursive approach with the condition of checking divisibility by 2 and 3, which is similar to the approach used in the original prompt.