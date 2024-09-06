```python
def triples_sum_to_zero(lst):
    sum_ trio = 0
    trio = []
    for num in lst:
        if sum([x for x in lst if x != num]) <= 0:
            sum_trio += num
            trio.append(num)
   
    return sum_trio == 0 and len(trio) == 3 or False
```
The above code defines a function triples_sum_to_zero that determines whether a given list lst has three distinct elements whose sum is zero.

It does this by initializing a sum_trio variable to accumulate the sum of the elements, and a trio variable to hold the elements. Then, it loops through each element in lst, checks if the sum of all elements except the current element is less than or equal to zero, and if so, adds the current element to both variables.

Finally, it returns True if there are exactly three distinct elements with a sum of zero, and False otherwise.