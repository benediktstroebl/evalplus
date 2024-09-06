```python
def starts_one_ends(n):
    num = 10 ** (n - 1)
    ones = num - 1
    ends_with_one = ones % 10
    starts_with_one = ones // 10
    return starts_with_one + ends_with_one
```
The function operates by determining the count of feasible numbers using the following calculation: If we take 10 as a basis (since there are 10 choices for each digit), there is only one number between 1 and 10 that starts with 1 (i.e., 11), and one number that ends with 1 (i.e., 10).

By extension, for every subsequent power of 10, starting with 10, there will be an additional number that starts with 1 and ten more that end with 1.

Therefore, to obtain the counts for a specific number of digits `n`, we utilize the following equations:
- Numbers that start with 1: `ones * 10^{(n-1)} / 10`
- Numbers that end with 1: `ones * 10^{(n-1)} % 10`

Where `ones` represents 10^{(n-1)-1}. Combining the above equations, we return their sum for the final result.

The recommended tests to ensure the function is operating correctly are:
```python
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 11
assert starts_one_ends(3) == 1113
assert starts_one_ends(4) == 11111415
assert starts_one_ends(5) == 1111111112526157
``` 

These tests cover different `n` values, ensuring that the function's answer makes sense in terms of the problem's rationale.