```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers, xs, as its input. It employs a list comprehension to filter out elements that have at least one even digit when converted to a string and then converted back to an integer with the int() function. The resulting filtered list is then sorted in increasing order using the sorted() function. To test this, we can create a list of positive integers with various digit configurations and pass it to the function, as shown in the example below:
```python
test_list = [15, 33, 1422, 1, 152, 323, 1422, 10]
print(unique_digits(test_list))
```
This will output:
```
[1, 15, 33]
```
The function successfully filters out elements with even digits, and the result is sorted as expected.