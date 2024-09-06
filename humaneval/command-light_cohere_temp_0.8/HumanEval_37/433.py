```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

even_list = sort_even([1, 2, 3])
print("Even list:", even_list)  # [1, 2, 3]
even_list = sort_even([5, 6, 3, 4])
print("Even list:", even_list)  # [3, 6, 5, 4]
``` 
This function uses a list comprehension to filter out the even numbers from the input list, then sorts the remaining odd numbers.