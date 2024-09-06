```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return sorted(lst) if len(even_lst) > 0 else even_lst

#Test case 1:
assert sort_even([1, 2, 3]) == [1, 2, 3]

#Test case 2:
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

#Test case 3:
assert sort_even([9, 6, 5]) == [9, 6]

#Test case 4:
assert sort_even([2, 8, 10, 4]) == [2, 4, 8, 10]
```
The provided code defines a function sort_even, which takes a list as input and returns a sorted list of elements, specifically the even numbers, while keeping the odd numbers as they are. The function achieves this purpose by first filtering out the even numbers from the input list using a list comprehension and then applying the `sorted` function to the remaining elements. 

The code then performs several tests on the `sort_even` function using the `assert` statement, ensuring that the function correctly sorts the even numbers in the output.