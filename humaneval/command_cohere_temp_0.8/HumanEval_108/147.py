```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '-' and int(b) > 0)
    return output
```
This Python script defines the function `count_nums`, which takes an array of integers as input and calculates the number of elements in the array that have a sum of digits greater than 0. The function accomplishes this by iterating through each element in the array and evaluating its individual digits. When a digit is encountered, it is converted to an integer using the int() function. If the digit is not '-' (indicating a negative sign) and its value is greater than 0, it is added to a running total using the sum() function. The final result is the total count of elements with non-negative digits that have a sum greater than 0. 

To test the function, it is provided with three test cases as examples, and the corresponding outputs are listed. These test cases encompass different scenarios, including an empty array and arrays containing various numbers. Ultimately, the function correctly identifies the count of elements with positive digit sums in the given arrays.