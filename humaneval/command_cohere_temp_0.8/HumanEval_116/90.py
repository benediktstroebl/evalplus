```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the actual number. The `sort` function will first sort the list based on the first element in ascending order, and then for numbers with similar number of ones, it will sort based on the second element, which is the actual decimal value of the number. The binary representation of numbers is achieved using the `bin` string method. Overall, this function follows the specified requirements and order of the integers as asked. 

Let's break down the key function `lambda x: (-bin(x).count('1'), x)`: 

1. `lambda x: `- this is a lambda function with a single parameter `x` that is being passed to the `sort` function for custom sorting. 
2. `bin(x)`  returns the binary representation of the integer `x` as a string. For example, `bin(6)` is `'110'` 
3. `.count('1')` counts the number of occurrences of `'1'` in the binary representation of the number, which gives the number of ones in the binary representation. 
4. `(-bin(x).count('1'), x)` returns a tuple with the number of ones in binary representation as the first element and the original number `x` as the second element. The `-` before the count of ones ensures that numbers with more ones appear first in ascending order. 

This function sorts the array first based on the number of ones in the binary representation in ascending order, and then for numbers with a similar number of ones, it sorts based on the actual decimal value of the number. 

Overall, this lambda function and the `sort` function provide an elegant and efficient solution to the problem. 

This approach has a time complexity of O(n log n) where n is the number of elements in the array, as per the [Python documentation on sorting](https://docs.python.org/3/reference/expressions.html#standard-function-calls).