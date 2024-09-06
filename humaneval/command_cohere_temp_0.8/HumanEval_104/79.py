```python
def unique_digits(x):
    odd = [int for int in x if any(int % 2 for int in str(int) if int.isdigit())]
    return sorted(odd)
```
```
The function unique_digits processes the list of integers x as follows:
1. A list of odd integers is generated using a list comprehension. This list contains all elements from x that have at least one odd digit in their decimal representation. The expression int for int in x generates a list of integers, and the any() function with the generator expression int % 2 for int in str(int) if int.isdigit() checks if any digit of an integer is odd.
2. The list of odd integers is then sorted in ascending order using the sorted() function and returned as the result.
```