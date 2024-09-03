```python
def solution(lst):
"""
You are given a list of integers. You need to find the largest prime number and return the sum of its digits.

:param lst:
:return: integer -- sum of digits of the largest prime number
"""
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = float('-inf')
    sum_of_digits = 0

    for num in lst:
        if is_prime(num) and num > max_prime:
            max_prime = num

        if is_super_prime(max_prime):
            sum_of_digits = sum(map(int, str(max_prime)))

    return sum_of_digits


def is_super_prime(n):
    """Check if a number is a prime and all its digits are prime as well"""
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if not is_prime(digit):
            return False
    return True
```