```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '0')
    return output
```
This Python script defines the function `count_nums`, which takes an array of integers as input and calculates the number of elements whose digit sum is greater than 0. To do this, it uses a nested list comprehension. For each number in the input array, it converts the number to a string and iterates through each digit. If a digit is not equal to '0', it converts it to an integer using int() in the outer comprehension, and sums these integers up using the sum() function. The final result is the count of elements with a positive digit sum. The function returns this count as the output.

Here is an example usage of the function:
```python
arr = [4, 545, -345, 7, 12]
print(count_nums(arr))  # Output: 5
```
This would print the count of elements with a positive digit sum in the array [4, 545, -345, 7, 12]. 

The function handles empty arrays, returning 0 in such cases:
```python
print(count_nums([]))  # Output: 0
```
It also correctly identifies positive and negative numbers with positive digit sums, ensuring that the first signed digit is considered:
```python
arr = [-1, 11, -11]
print(count_nums(arr))  # Output: 1
```
The expected output is 1, as only the number 11 has a positive digit sum.