Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    bin_str = bin(n)[2:]
    sum_list = [int(x) for x in bin_str if x != '0']
    return '{0:b}'.format(sum(sum_list))
```
This script defines a function `solve(n)` that takes an integer `n` as its argument and returns the binary string representation of the sum of its digits. 

Here's how it works:
- `bin_str = bin(n)[2:]`: This converts the integer `n` to a binary string, but it uses `bin()` to do so. The `[2:` clause is used to skip the leading '0b' of the result.
- `sum_list = [int(x) for x in bin_str if x != '0']`: This converts the binary string to a list of integers, where each integer represents a digit in binary. Then it filters out the '0's from the list.
- `return '{0:b}'.format(sum(sum_list))`: This converts the sum of the digit integers back to a binary string and returns it.

The output of the given examples in the prompt will be:
```
1
110
1100
```
This solution is concise and achieves the desired result. It leverages Python's built-in binary conversion methods and list comprehensions for a efficient and effective solution.