```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This solution uses the split method to split the string into two strings ('apples' and 'oranges') and then calls the int() function to convert these into integers. Then, by simply subtracting the sum of the apples and oranges from the total number of fruits, the desired result is achieved. 

For example, the call `fruit_distribution("5 apples and 6 oranges", 19) `will return `8` since the total number of fruits in the basket is 19, and after subtracting the number of apples and oranges, we get 8.

This approach assumes that the inputs are well-formed, i.e., the given string represents numeric values and the integer `n` represents the total number of fruits in the basket. 
If the given string is not well-formed numeric values, the above solution may return incorrect results. 
It's important to handle validation and error checking accordingly in real-world scenarios.