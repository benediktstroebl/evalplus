```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Test Cases
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1))
print(x_or_y(n2, x2, y2))
```

In the above code, the is_prime function is a helper function that checks if a number is prime or not. The x_or_y function uses this helper function to determine whether to return x or y based on the primality of n. The test cases are provided to demonstrate the function's correctness against specific input. 

The script passes the tests provided in the problem statement and outputs the expected values: 
```
34
5
``` 

The code is self-contained and does not rely on any external variables or modules, making it portable and maintainable. 
If needed, the code can easily be adapted to serve different purposes or integrate into larger projects. 
Feel free to modify it to suit specific needs or further clarify specific details. A more in-depth explanation of the code may be beneficial for learning or for providing a basis for code reviews or optimization.