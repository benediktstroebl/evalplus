```python
def unique_digits(x):
    odd = [int for int in x if any(int % 2 for int in str(int) if int.isdigit())]
    return sorted(odd)
```
```
The function unique_digits processes the list x as follows:
1. A list of odd integers is created via a list comprehension. This list will contain all elements from x that have at least one odd digit. This is done using the any function combined with a generated list from int in str(int) for int in str(int) if int.isdigit(). The int.isdigit() function checks if the integer is a digit, and the int in str(int) expression extracts individual digits from the integer. 

For example, let's take the list element '325' from the input list x. The expression int in str(int) produces the list ['3', '2', '5'], while int.isdigit() returns True for all these elements. Then any(int % 2 for int in str(int) if int.isdigit()) evaluates to True, since the odd digit '3' yields int % 2 == 1, while the even digits '2' and '5' yield int % 2 == 0, and consequently any of them satisfies the condition.

2. The created list of odd integers is then sorted in ascending order using the sorted function and returned as the result.
```