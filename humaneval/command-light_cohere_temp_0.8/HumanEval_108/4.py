```python
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    Returns None if the particular with negative numbers 
    """
    # initialize count of numbers with sum > 0 to 0
    c = 0
    for x in arr:
        sum_ = sum(map(int, str(x)))
        if sum_ > 0:
            c += 1
    return c
# Example usage
arr = [1,2,3,4,5,6]
print(count_nums(arr)) 
``` 
This code defines a Python function `count_nums` that takes an array of integers as input and returns the count of elements that have a sum of their digits greater than 0. The function initializes a count of such numbers to 0 and then iterates through each element in the input array. It calculates the sum of the digits of each element by converting it to a string and then using the `sum` function, it adds up the digits and checks if the sum is greater than 0. If the sum is positive, the function increments the count of numbers with sum greater than 0. If the sum is negative, the function doesn't count the number. 

The output of this code will be the count of numbers with sum greater than 0 in the input array.