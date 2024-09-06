```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers xs as input and returns a sorted list of all elements in xs that do not contain any even digits. The function checks if none of the digits in the string representation of an integer is even, using the expression int(y) % 2 == 0 for y in str(x), for every x in xs. The resulting list of integers is then sorted in increasing order using the sorted() function and returned.

Here is an example of how to use the above code:
```python
test_list = [15, 33, 1422, 1, 152, 323, 1422, 10]
print(unique_digits(test_list))
```
This would print:
```
[1, 15, 33]
```
This is correct as the list test_list contains elements with the digits 1, 5, and 3. These are the only integers in the list that do not contain any even digits. Thus, the function unique_digits() would return the list [1, 15, 33] as the output.