```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test cases
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1))  # Output: 34
print(x_or_y(n2, x2, y2))  # Output: 5
```

In the above code, the is_prime function checks if a number is prime or not. The function uses a simple algorithm to iteratively check if the number is divisible by any number from 2 to the square root of the number. If the number is divisible by any integer in this range, it returns False, indicating that the number is not prime. Otherwise, it returns True. 

The x_or_y function takes three arguments: the input number n, and two values x and y. It first checks if n is prime using the is_prime function. If n is prime, it returns x; otherwise, it returns y.

The test cases at the end demonstrate the function's behavior for two different inputs, and the printed outputs are as expected. 

Feel free to modify the test cases to evaluate the function under different scenarios. 
If you have any further questions or requests, please let me know!