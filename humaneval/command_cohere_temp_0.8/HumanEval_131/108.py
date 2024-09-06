```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            prod *= int(digit)
    return prod
```

This problem can be solved by iterating through each digit in the integer `n` and multiplying the odd digits while incrementing a counter for even digits. The final product will be the sum of the odd digit multiplications, and the count of even digits will be 0. To better understand this, let's break down the code:
1. We define a variable `prod` which will accumulate the product of odd digits. This is initialized to 1 as an empty product of any one odd digit will yield 1.
2. Then we loop through each digit in the string representation of the integer `n`.
3. Within the loop, we check if the current digit is odd using the modulo operator (`%`). If it's odd, we multiply the current value of `prod` by the int representation of the current digit. 
4. If all digits are even, the product will be 0 as every digit will yield 0 when multiplied, and `prod` will be multiplied by 0 many times. Thus the final answer is 0 in this case. 

This algorithm is efficient and has a time complexity of O(n), where n is the number of digits in the given integer `n`.