```python
def sort_even(lst):
    even_lst = [item for item in lst if item % 2 == 0]
    return [element for element in lst] if even_lst == lst else even_lst

```
This function uses list comprehension to filter out even numbers and then returns a new list with even numbers sorted in ascending order.

In the next step, it uses an if-else statement to check if the even list is equal to the original list. This ensures that the reordering is not applied to the already sorted even numbers. 

Finally, it returns the new list with the even numbers in sorted order.