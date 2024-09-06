```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # denominator
            k = i     # numerator
            # the largest divisor is the last divisor
            if j > k:
                return j
            elif j == k:
                return k
    return 1  # return 1 if no number can divide the given number n

# tests
assert largest_divisor(15) == 5
assert largest_divisor(8) == 4
assert largest_divisor(1) == 1
``` 

This Python script defines a function called `largest_divisor` that takes in an integer value, `n`, as input. This function iterates through all the integers between 1 and `n` (inclusive), and for each integer `i`, it checks if `i` can divide `n` evenly. In other words, it checks if the division `n / i` produces a whole integer result (`n // i`). The function then determines if the current divisor `i` is the largest one encountered so far. It returns the largest divisor `k` if `n // k` is the same as `k`; otherwise, it returns the largest denominator `j`. 

The script also includes test cases to validate the functionality of the `largest_divisor` function. Specifically, it tests the function's outcomes for the values 15, 8, and 1, asserting that the function returns the expected outputs of 5, 4, and 1, respectively. 

The function ultimately returns 1 if no number can divide `n` evenly. 

This solution is quite efficient, as the worst-case complexity is O(n).  This efficiency arises from the fact that the loop iterates through numbers between 1 and `n`, and for each iteration, the division and modulo operations are O(1). Thus, the complexity of the entire loop is O(n).  Additionally, the solution wastes no excess memory, making it an efficient approach for this problem.