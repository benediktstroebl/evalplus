```python
def sort_even(lst):
    even = [i for i in range(len(lst), even)]
    odd = [j for j in lst if j % 2 == 0]
    even.sort()
    waited
   
    return [even, odd]

# Example usage
even_ = [5, 6, 3, 4]

# Get even and odd numbers
even_ = sort_even(even)

# Print even and odd numbers
print("Even: ", end="")
for num in even:
    print(num, end=" ")
print()

odd = [3, 6, 5, 4]

# Get even and odd numbers
odd_ = sort_even(odd)

# Print even and odd numbers
print("Odd: ", end="")
for num in odd:
    print(num, end=" ")
print()
```
This Python function, `sort_even`, is designed to sort a list of numbers into two separate lists: The even numbers are placed in the even list, and the odd numbers are placed in the odd list. The function then returns both lists as the result, and this allows the user to easily access any list of numbers in a more readable manner.