```python
def sort_even(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    odd.append(num)
    lst = [even, odd]
    return lst

# Test the function with a sample list
test_sort_even = []
test_sort_even.append([1, 2, 3])
test_sort_even.append([5, 6, 3, 4])
test_sort_even.append([5, 6, 5, 4])
test_even = sort_even(test_sort_even)
print(test_even)
```

This script defines a function `sort_even` that sorts a list of numbers into two separate lists: The function works by first creating an empty list called `even` to store even numbers, and an empty list called `odd` to store the odd numbers. Then, it iterates through the list of numbers and assigns them to the appropriate lists based on their parity. Finally, the function returns a list of lists, where the even numbers are in `even` and the odd numbers are in `odd`.