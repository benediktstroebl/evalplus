```python
def sort_even(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    lst = even_lst
    return lst

# Test the function with a list of numbers
test_sort_even = []
test_sort_even.append([range(6,0,-1))
test_sort_even.append([1,2,3,4,5,6])

# Call the function and store the result in a list
result_sort_even = sort_even(test_sort_even)

# Print the result
print(result_sort_even)

``` 
This script defines a function `sort_even` that takes a list and returns a new list that sorts the odd indices of the original list to the end, and keeps the even indices as they are. The test cases pass the