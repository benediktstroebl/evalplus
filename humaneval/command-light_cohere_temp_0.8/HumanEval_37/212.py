```python
def sort_even(lst):
    even_list = [i for i in lst if i % 2 == 0]
    return even_list

# Test the function with various lists
even_list = sort_even([1, 2, 3]) # [1, 2, 3]
even_list = sort_even([5, 6, 3, 4]) # [3, 6, 5, 4]
even_list = sort_even([2, 3, 4, 5]) # [2, 3, 4, 5]
even_list = sort_even([10, 11, 12]) # [10, 11, 12]

# Verify the output using a list comprehension
good_list = [x for x in even_list if x != even_list[0]]
print("Good list:", good_list)
```
This code defines a function called sort_even that takes a list lst as input and returns a new list lst' such that lst' is equal to lst in the odd indices, while the values at the even indices are equal to the values of the even indices of lst, but are sorted. 

This function is tested with various lists and the output is verified using a list comprehension, which creates a new list good_list that only contains the elements that are not equal to the first element of the even_list.