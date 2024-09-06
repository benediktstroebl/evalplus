```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == num2 * den1
```

The function `simplify()` takes two fractions as string inputs represented in the format of a divide operation i.e. `("/")`. It then splits each string into two parts where the first part is the numerator and the second part is the denominator. It then maps these parts into integers using the `int()` function and checks if the product of the numerator of n and the denominator of x, is equal to the product of the numerator of x and the denominator of n. If the condition is true, the function returns True, and if not, it returns False.

This problem can also be solved using regex and relies on extracting information from the strings in the same manner as the above code. However, it is worth noting that the above solution is more efficient and does not require any additional modules. 

This Python script solves the problem and would yield the correct results when applied to the test cases provided.