```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Unit tests
tests = [
    (7, 34, 12, 34),
    (15, 8, 5, 5),
    (101, -5, 5, 5),
    (4, '', '', 'Should be prime'),
    (0, '', '', 'Should be prime'),
    (2, '', '', 'Should not be prime'),
]

for n, x, y, expected in tests:
    result = x_or_y(n, x, y)
    if result != expected:
        print(f"For inputs {n}, {x} and {y}, expected {expected} but got {result}")
``` 

The code consists of two parts. The first part is a `is_prime` function that checks whether a given number is prime or not. The second part is the `x_or_y` function that returns the value of `x` if the number is prime and `y` otherwise. 

The `is_prime` function is a basic primality test that checks whether the number is less than or equal to 1, which would immediately return false. For the numbers equal to 2 and 3, it also returns false. Then, the code checks whether the number is divisible by 2 or 3, and if so, it returns false. For larger numbers, it iterates through the numbers 5, 7, 11, 13, 17, 19, and so on, gradually increasing the step to 6 at a time, checking if the number is divisible by any of them. Finally, if none of the conditions are met, it returns True. 

The `x_or_y` function utilizes the `is_prime` function to determine whether a number is prime. If the number is prime, it returns the value of the `x` parameter. If not, it returns the value of the `y` parameter. 

The unit tests are created to check various scenarios of the `x_or_y` function and demonstrate how the function should work.  The function is applied to a list of test cases, and the actual output is compared to the expected output. If the outputs do not match, an error message is printed, indicating that the function did not perform as expected.  This approach helps to ensure the correctness of the code and verifies that the function works correctly for a variety of inputs.