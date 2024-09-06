```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))

test_list2 = "Hello World"
print(unique(test_list2))

test_list3 = [1, 2, 3, 4, 5, 6]
print(unique(test_list3))

test_list4 = [['a', 'b', 'c']
print(unique(test_list4))

test_list5 = [0, 2, 3, 4, 5, 6, 7, 8, 9]
print(unique(test_list5))
``` 
This code defines a function `unique` that takes in a list `lst` as an argument. The function creates a set `seen` to keep track of unique elements encountered in the list. Then, for each element in `lst`, the function checks if it's already in `seen`. If not, it's added to the list `result` and then returned.

The function then uses a for loop to iterate through the list and adds each element to `seen` if it hasn't been seen before. The function then adds the elements in `result` to the return value.