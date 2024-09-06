```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test the max_element function
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This script defines a function max_element that calculates the maximum element in a list. The function first checks if the max_element is passed a list of numbers and if it's the list is empty or contains only positive numbers, it returns -inf.

The not_positive function tests whether the list contains only positive numbers. The max_element function then returns the maximum value of all elements in the list.

The test code then calls the function with a list of numbers and prints the result. 

Let's break down the code step by step:
1. **def max_element(lst):**- This function takes a list lst as input and aims to return the maximum element in the list.
2. **if not_positive(lst):**- This condition checks whether the input list lst is empty or contains only positive numbers. If this is the, it returns the special value float('-inf'), which means that no element in the list is greater than negative infinity.
3. **return max(lst)** - This line uses the built-in Python function max to find the maximum element in the list. The max function takes an list as its argument and returns the highest value of all elements in that list.
4.  ** ** **- The way that the maximum element is found, the function returns that value.
5. The function does not consider negative numbers, zero, or any other values.
6.  ** ** ** **def not_positive(lst):**- This function tests whether the list lst contains only positive numbers. If this is the case, it returns True, indicating that the list contains only positive numbers.
7.  ** ** ** **all(x > 0 for x in lst):** This line uses the Python built-in function all to check whether all elements in the list are greater than zero. If all elements elements are greater than zero, the function returns True.
8.  The **test the **max_element(lst):** This line calls the function max_element with the list lst as its argument. The function returns the maximum element in the list, which is stored in the variable max_element.
9.  ** ** ** **print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))** - This line calls the max_element function with a list of numbers and prints the result, which is the maximum element in the list.

The output of the code will be the value of the maximum element in the list, which in this case is 123.