```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [y for y in lst if y % 2 != 0]
    lst[:] = [x for x in even] + [y for y in odd]
    return lst

#Test 1
test_list = [1, 2, 3]
result = sort_even(test_list)
print(result)

#Test 2
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
print(result)
```
This Python code defines a function `sort_even` that takes a list as an argument and sorts it such that the even elements appear before the odd elements. The function creates two separate lists: `even` and `odd`, which contain elements based on whether their indices are even or odd, respectively. Then, it reordersizes the list by inserting the elements from `even` and `odd` into the original list in corresponding positions, effectively sorting the list by even elements first. The function is tested using two test cases, and the results are printed to the console.