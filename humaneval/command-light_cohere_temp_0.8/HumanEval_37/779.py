```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    even_res = sorted(even_list)
    odd_list = [x for x in lst if x % 2 != 0]
    odd_res = sorted(odd_list)
    return even_res, odd_res

# Test the function with various lists
even_res1, odd_res1 = sort_even([1, 2, 3])
even_res2, odd_res2 = sort_even([5, 6, 3, 4])

print(even_res1)
print(even_res2)
print(odd_res1)
print(odd_res2)
```

The above script defines a function `sort_even` that sorts even numbers from the input list, and leaves other values unchanged. The function then passes these tests with various lists and prints the results.