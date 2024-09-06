```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        return_value = 3
        for i in range(2, n):
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if int(j) > i or int(j ** i) > n:
                    is_prime = False
                if is_prime:
                    break
            return_value = int(i ** 0.5)
        elif is_prime:
                return_value += 1
        return return_value
``` 
Do you want help with anything else?