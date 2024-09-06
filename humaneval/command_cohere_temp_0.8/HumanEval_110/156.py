```python
def exchange(lst1, lst2):
    odd = next((el for el in lst1 if el % 2 != 0), None)
    even = next((el for el in lst2 if el % 2 == 0), None)
    if odd is None or even is None:
        return "YES"
    return "NO"
```
The function `exchange()` takes two lists, `lst1` and `lst2` as input and returns a string indicating whether the elements can be exchanged between the two lists to make `lst1` contain only even numbers. The function utilizes the `next()` function to retrieve the first odd number from `lst1` and the first even number from `lst2`, respectively.

If either the odd number or the even number is `None`, it implies that at least one of the lists contains only even numbers, and an exchange would not be necessary. In this case, the function returns "YES." However, if both the odd number and the even number are retrieved successfully, it means that an exchange can be performed, and the function returns "NO."

This approach avoids unnecessary complexity and provides a clear and efficient solution to the problem. The function's logic is straightforward, making it easier to understand and maintain, aligning with good coding practices. The function is also robust, as it handles potential edge cases where one or both lists contain only even or odd numbers.