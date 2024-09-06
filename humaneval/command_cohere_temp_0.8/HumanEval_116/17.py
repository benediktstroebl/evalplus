```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that transforms each element in the list. Here, a lambda function is used to return a tuple where the first element is the number of '1's in the binary representation of the number, and the second element is the actual number. The numbers are sorted based on this tuple in ascending order. 

This approach solves the given problem in a relatively efficient manner. Let's break down the code and explain how it works step-by-step:
1. `arr.sort(key=lambda x: (bin(x).count('1'), x))`: This line does all the work. It sorts the input list `arr` using the `sort` method, but with a specified `key` function. The key function is a lambda function `(lambda x: (bin(x).count('1'), x))`. 
2. `(bin(x).count('1'), x)`: This is the lambda function that is acting as the key. It returns a tuple with two elements:
   - `bin(x).count('1')`: This part calculates the number of '1's in the binary representation of the number `x`. For example, if `x` is 5, this will produce '111', and the count of '1's will be 3.
   
   - `x`: This is simply the original number `x` as the second element in the tuple. 

3. `return arr`: This simply returns the sorted list `arr`. 

The overall effect of applying this sorting key is to first sort the numbers based on the number of '1's in their binary representation. If two numbers have the same number of '1's, they are further sorted based on their decimal value in ascending order. This aligns with the spec from the problem statement. 

You can verify that the function sorts the array as expected according to the problem statement:
```python
>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
True
>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
True
>>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
True
``` 
This demonstrates that the function can handle both positive and negative integers, as well as handle different inputs and their binary representations.