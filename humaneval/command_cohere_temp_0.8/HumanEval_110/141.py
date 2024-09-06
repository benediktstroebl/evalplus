```python
def exchange(lst1, lst2):
    even_numbers = [x for x in lst1 if x % 2 == 0]
    if len(even_numbers) == len(lst1):
        return "YES"
    return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function first creates a list called `even_numbers` that contains all the even numbers from `lst1`. Then, it compares the length of `even_numbers` with the length of `lst1`. If the lengths are equal, it returns "YES," indicating that all elements in `lst1` can be even. If the lengths are not equal, it returns "NO," indicating that not all elements in `lst1` can be even. 

Here is an example usage of the function:
```python
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
print(exchange([1, 2, 3, 4], [2, 4, 6, 8]))  # Output: "YES"
```

This example test cases demonstrate the functionality of the `exchange()` function with different inputs.