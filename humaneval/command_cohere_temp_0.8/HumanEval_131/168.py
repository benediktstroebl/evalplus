```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This problem can be solved by converting the input n into a string to iterate over each digit. We check if each digit is odd or even, updating a product variable `prod` that accumulates the product of odd digits. The function returns 0 if all digits are even, and the product of odd digits otherwise. 

This solution is efficient because it uses only a few variables, a for loop, and basic arithmetic operations, resulting in a time complexity of O(D), where D is the number of digits of the given input.