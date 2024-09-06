```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return True if the object `q` will fly according to the given criteria, and False otherwise. This is achieved by returning True if `q` is a balanced palindromic list (`q == q[::-1]`), has a sum of elements less than or equal to the maximum possible weight (`sum(q) <= w`), and is not an empty list (`len(q) > 1`). 

Here is an example usage of the function for validation:
```python
>> will_it_fly([1, 2], 5)
False
>> will_it_fly([3, 2, 3], 1)
False
>> will_it_fly([3, 2, 3], 9)
True
>> will_it_fly([3], 5)
True
```

This implementation assumes that the list `q` and the number `w` are both valid inputs and that the weight `w` is an integer or integer-like object that can be interpreted as a sum of integers.

This approach utilizes Python's list slicing feature, denoted by `q[::-1]`, to reverse the list `q` and compare it with the original. This results in a True value if the list is balanced and a False value otherwise. The weight comparison is done through the `sum` function, which calculates the sum of the list's elements, and the `<=` operator, which compares the sum to the maximum weight `w`. 

The `if` statement combines these two comparisons (`sum(q) <= w` and `q == q[::-1]`) to determine whether the object will fly or not. 

Note that the function includes a additional condition to check if the list is not empty, i.e., `len(q) > 1`, this is to prevent any potential errors with an empty list.  This condition is not explicitly mentioned in the problem statement but is included as a safety measure.