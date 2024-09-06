```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return True if the object `q` will fly, and False otherwise. The object `q` will be considered flying if it is balanced (a palindrome) and the sum of its elements is less than or equal to the maximum possible weight `w`. The weight of the object is the sum of its elements, and the maximum possible weight is the value of the second parameter.

The function checks that the length of the list is greater than 1 to assure that is not just a single element, and that the sum of the elements in the list is less than or equal to the maximum possible weight. It also checks that the list is a palindrome by comparing it to its reverse. If all these conditions are met, the function returns True; otherwise, it returns False.