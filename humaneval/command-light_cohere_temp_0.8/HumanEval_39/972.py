```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        limit = 2
        result = 0
        while limit * limit <= n:
            temp = 0
            i = 2
            while i <= limit:
                if n % i == 0:
                    break
                temp += i
            result = temp
            limit += 1
        return result

# Test case
print(prime_fib(10))
 ``` 
The above Python script defines a function called `prime_fib` that returns the n-th Fibonacci number which is also prime. 

This function uses a loop to generate the Fibonacci numbers and checks for divisibility by limiting the values of i, until it exceeds the square root of n.