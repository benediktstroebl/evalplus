```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function `lambda x: (bin(x).count('1'), x)` which first counts the number of '1's in the binary representation of the number `x`, and then returns `x` as a secondary key in case two numbers have the same number of '1's. The `sort` function will arrange the array according to these parameters in ascending order. 

This solution efficiently solves the problem and provides a sorted array as outlined in the problem statement. Let's break down the solution to this problem:
1. Understanding the Problem: We are given an array of non-negative integers and we need to sort it according to the number of ones in their binary representation, in ascending order. For integers with a similar number of ones, we sort based on their decimal value.
2. Key Argument in Sort: The `key` argument in Python's `sort` function allows us to specify a custom function to define the sorting key for each list element. This function returns a tuple comprising the number and the variable to be sorted. 
3. Lambda Function: The lambda function `lambda x: (bin(x).count('1'), x)` is shorthand for a function that takes an argument `x` and returns a tuple of two items: the first is the number of '1's in the binary representation of `x`, and the second is `x` itself. 
4. Bin Function: The `bin` function converts a number to a binary representation. The string `bin(x)` provides the binary representation of the variable `x`. 
5. Count '1's: The .`count('1')` method counts the number of occurrences of the substring '1' in the binary representation. This gives us the number of ones in the binary representation. 
6. Sorting Criteria: The numbers are first sorted based on the count of ones in the binary representation. If there are similar numbers, they are sorted based on their decimal value in ascending order. 
7. Descending Order Consideration: It's vital to note that the binary representation of a number doesn't contain information about the sign of the number. This strategy works appropriately because we are given that the array just contains non-negative integers. 

This approach leverages the `key` parameter in Python's `sort` function and the properties of binary representation to efficiently solve the problem.