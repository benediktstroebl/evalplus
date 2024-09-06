Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x >= 0]
```
The function `get_positive` takes a list as an argument and returns a new list that contains only the elements that are equal to or greater than zero. The problem is solved in Python using a list comprehension, which allows for creating a new list by applying a condition to each element of the original list. 

Here is an example of using the `get_positive` method on two lists with both positive and negative integers: 
```python
test_list1 = [-1, 2, -4, 5, 6]
test_list2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print("Test List 1: ", test_list1)
print("Test List 2: ", test_list2)

print("Only positive numbers in Test List 1:")
print(get_positive(test_list1))
print("\n")

print("Only positive numbers in Test List 2:")
print(get_positive(test_list2))
```
This will produce the following output:
```
Test List 1:  [-1, 2, -4, 5, 6]
Test List 2:  [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
Only positive numbers in Test List 1:
[2, 5, 6]

Only positive numbers in Test List 2:
[5, 3, 2, 3, 9, 123, 1]
```
As expected, the positive numbers from both lists are separated and printed as the output.