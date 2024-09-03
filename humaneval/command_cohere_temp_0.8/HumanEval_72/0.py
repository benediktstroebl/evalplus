```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will fly, and False otherwise. The object q will fly if it is balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w. The function uses a logical operator to check if the list is palindromic by comparing it to its reversed version. It also compares the sum of the list of characters to the maximum possible weight w to see if the object would be able to fly in terms of weight. If both of these conditions are met, the function returns True, else it returns False. 

Here is an example usage of the function:
```python
print(will_it_fly([3, 2, 3], 9))  # This will print: True
print(will_it_fly([1, 2], 5))  # This will print: False
``` 

The first example will print True as the list is both palindromic and the sum of its elements (6) is less than the maximum possible weight of 9. However, in the second example, the sum of the elements is 3 which is less than the maximum possible weight of 5, but the list is not palindromic hence the function will return False.