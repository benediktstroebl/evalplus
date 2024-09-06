```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The function `digitSum` uses the sum function to calculate the sum of the digits in the string. The map function transforms each character in the string to its corresponding integer value. The filter function filters out the non-digit characters from the string, leaving only the digits. 

This solution approaches the problem by removing non-digit characters and calculating the sum of the digits. It provides an efficient and straightforward way of obtaining the desired result. 

The code is encapsulated in a self-contained function, making it easy to use and test. Simply provide a string as a parameter, and the function will return the sum of the upper case characters' ASCII codes.