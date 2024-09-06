```python
def sort_even(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    odd.append(num)
   
    return [even, odd]

# Example usage
even_list = [5, 6, 3, 4]
odd_list = [1, 2, 3]
result = sort_even(even_list)
print("Even list:", result)
result = sort_even(odd_list)
print("Odd list:", result)
```

This code defines a function called sort_even, which takes a list lst as input and returns two lists: The function separates the input list into even and odd numbers and then returns the respective lists. This is a then can be passed to other functions to perform further operations or testing.