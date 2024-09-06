```python
def sort_even(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    even_lst = sorted(even_lst)
    return even_lst

# Test case 1
print("Test case 1: " +[5, 6, 3, 4] +")
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]

# Test case 2
print("Test case 2: " +[1, 2, 3] +")
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]

# Test case 3
print("Test case 3: " +[4, 5, 6] +")
print(sort_even([4, 5, 6]))
# Expected output: [4, 5, 6]
```
The code defines a function `sort_even` that takes a list as an argument and sorts the even integers from the list. This function creates a `even_lst` to hold the even integers and then sorts this list. The function then returns the `even_lst`, which contains the sorted even integers.

The test cases show how the `sort_even` function can be used to sort even integers in a list. The expected output of each test case is the list with the even integers correctly sorted.