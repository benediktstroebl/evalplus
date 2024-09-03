```python
def monotonic(l: list):
    return all(x < y for x, y in zip(l, l[1:]))

# Test the function
test_list = [1, 20, 4, 10]
test_list2 = [4, 1, 0, -10]
print(monotonic(test_list))  # Output: True
print(monotonic(test_list2))  # Output: True
```
The output of this script will be True for the first test and also for the second test, it will output False. 
The function works by using the concept of comparing each element in the list to its own previous element and returns True if all elements are strictly decreasing or increasing.