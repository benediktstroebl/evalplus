```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list. Here, a lambda function is used to return a tuple where the first element is the number of '1's in the binary representation of the number, and the second element is the decimal value of the number. The sort is performed based on this tuple.

The code implements the custom sorting described in the problem statement and should provide the expected output for the example inputs provided. 
Let's break down how the lambda function works:
1. `lambda x: (bin(x).count('1'), x)`: This part of the lambda function takes each element `x` in the input list and does a few things:
- `bin(x)` converts the decimal number `x` to a binary string representation. 
- `.count('1')` counts the number of occurrences of the character '1' in the binary string. This effectively counts the number of binary '1's in the binary representation of the number. 
- The lambda returns this count as the first element in a tuple. 

2. `arr.sort(key=lambda x: (bin(x).count('1'), x))`: This sorts the input list `arr` using the key lambda function. The lambda function returns a tuple `(count_ones, decimal_value)` for each number in the list. The numbers are sorted primarily based on the `count_ones` and secondarily based on the `decimal_value` if two numbers have the same count of ones. 

So, in summary, this lambda function works by converting each number to its binary representation, counting the ones, and returning this count along with the original number. This allows the numbers to be sorted first by their binary "ones" count and then by their decimal value if they have the same number of ones. 

Please note that this implementation assumes that the input array only contains valid integer values. If the input array contains non-integer values or invalid inputs, the function may raise an error or return incorrect results.