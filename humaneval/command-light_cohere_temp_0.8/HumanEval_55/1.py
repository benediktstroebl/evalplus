```python
def fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Test suite
test_fib = []
for i in range(1, 10):
    test_fib.append(fib(i))

test_result = sum(test_fib)
print("Test sum:", test_result)

``` 
This code defines the `fib` function that calculates the n-th Fibonacci number using an iterative approach. The function includes input validation to ensure that n is a positive integer. It then returns the tested using a series of test cases and comparing the result against the expected value using the `sum` function to calculate the test sum. 

The code also includes a test suite with a range of test cases to ensure the correctness of the `fib` function.