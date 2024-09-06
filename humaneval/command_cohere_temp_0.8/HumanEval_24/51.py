```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i > i:
            return i
    return 1
```
The function iterates through numbers from 1 to `n` and returns the largest number that divides `n` evenly, but is still smaller than `n`. This is done using the `range` function and checking if the current number `i` fulfills two conditions: 1. `i` divides `n` evenly (`n % i == 0`) and 2. Dividing `n` by `i` results in a number smaller than `i` (`n // i > i`). The latter ensures that the largest divisor is not `n` itself, but a smaller number.  For example, the largest divisor of `15` is `5`. 

To further clarify, let's break down the reasoning behind the code:
- The `for` loop iterates through numbers from `1` to `n`.
- For each number `i`, we check if `i` is a divisor of `n` (i.e., `n` is evenly divisible by `i`). This is done using the modulo operator `%`. If `n % i == 0`, it means that there is no remainder left when dividing `n` by `i`, indicating that `i` is a divisor of `n`.
- Additionally, we ensure that dividing `n` by `i` results in a number smaller than `i` (`n // i > i`). This helps rule out `n` itself as a potential largest divisor. If `n` divided by `i` yields a larger number, it means there is a larger divisor that still maintains the condition of dividing `n` evenly.
- If the above conditions are met for any `i` in the loop, the function returns `i`, which represents the largest divisor of `n`. If no suitable divisor is found in the loop, the function returns `1` as the default largest divisor. 
To further test the function, you can execute the following code, which checks the correctness of the function for a few test cases:
```python
test_cases = [15, 24, 36, 48]
expected_results = [5, 12, 18, 16]
for case, expected in zip(test_cases, expected_results):
    result = largest_divisor(case)
    assert result == expected, f"For n={case}, the largest divisor expected={expected}, found={result}"
```
You can add more test cases to `test_cases` and `expected_results` to validate the function further.