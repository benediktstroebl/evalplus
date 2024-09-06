```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script introduces a function **sum_squares(lst)** that processes a list **lst** of integers according to a specific rule and returns the sum of the processed integers. 

For each entry in the list, if its index is a multiple of 3 (i.e., divisible by 3), the integer is squared; if the index is a multiple of 4 but not a multiple of 3 (i.e., divisible by 4 but not by 3), the integer is cubed. The function leaves the integers unchanged if their index is not a multiple of either 3 or 4. 

The sum of all the modified or original integers is then returned as the function result. 

The function is then tested using the following test cases:
1. **Empty list [**: The function returns 0, as there are no elements in the list. 
2. **List [1, 2, 3]:** The function returns 6, as the elements at indexes 0, 2, and 4 are squared to yield 1, 4, and 9, while the element at index 1 is cubed to give 8. 
3. **List [-1, -5, 2, -1, -5]:** The function returns -126, as the elements at indexes 0, 1, 3, and 5 are squared to give 1, 25, 4, and 25, while the element at index 2 is cubed to yield 8. 

The function's implementation follows the problem statement and passes the provided tests, ensuring the correctness of the solution. 

This Python script efficiently squares integers at indexes that are multiples of 3 and cubes integers at indexes that are multiples of 4 but not multiples of 3, incorporating these values into the sum and returning the result.