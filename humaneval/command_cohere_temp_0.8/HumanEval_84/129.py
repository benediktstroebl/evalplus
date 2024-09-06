Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return '{0:b}'.format(sum(int(d) for d in s))
```
This function takes a positive integer `n` as its argument and returns the total sum of its digits in binary. It converts the integer to a string, iterates through its digits, converts them to integers, and sums them. Finally, it uses `format()` with `{0:b}` to convert the sum to a binary string and returns the result.  This solution utilizes string formatting techniques and Python's sum function and str.format() method to achieve the desired result in a concise manner. 

You can test this function by calling it with various input values to ensure it behaves as expected. For example:
```python
# Test Case
assert solve(1000) == '1'
assert solve(150) == '110'
assert solve(147) == '1100'
```
Let's break down the solution and explain it step by step for better clarity:
1. **def solve(n)**: This line defines a function called solve that takes a single parameter n, which represents the positive integer for which we want to calculate the sum of digits in binary.
2. **s = str(n)**: The str() function is used to convert the integer n to a string. This conversion is necessary because we need to manipulate individual digits, and converting to a string makes this easier. The result is stored in the variable s.
3. **return '{0:b}'.format(sum(int(d) for d in s))**: This is the crux of the solution. It uses a combination of string formatting and Python's built-in functions to achieve the desired result. Here's what's happening:
4. **sum(int(d) for d in s)****: This is a generator expression that iterates through each digit d in the string s, converts each digit to an integer using int(), and sums these integers. The result is a sum of the individual digits of the original integer n.
5. **'{0:b}'.format(** This uses the format() function to convert the sum of digits, which is an integer, to a binary string. The {} placeholders indicate where the values will be inserted.
6. **return <result>****: The formatted result, which is a binary string representing the sum of digits, is returned as the output of the solve() function.

In summary, this solution uses a combination of Python's string formatting, conversion, and built-in functions to achieve the desired result in a concise and elegant manner.