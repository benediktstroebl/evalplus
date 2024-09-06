```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst if even_lst != [] else [x for x in lst if x % 2 == 0] + [x for x in lst if x % 2 != 0]

# Test case 1: [1, 2, 3] -> [1, 2, 3]
test1 = [1, 2, 3]
result1 = sort_even(test1)
assert result1 == [1, 2, 3]

# Test case 2: [5, 6, 3, 4] -> [3, 6, 5, 4]
test2 = [5, 6, 3, 4]
result2 = sort_even(test2)
assert result2 == [3, 6, 5, 4]

# Test case 3: throw an error, odd number
test3 = [1, 2, 3, 4]
with raises(TypeError):
    sort_even(test3)
``` 
The code defines a function `sort_even` that takes a list as input and returns a sorted list of even numbers. It achieves this by creating an empty list `even_lst` to store the even elements and then iterating through the input list to populate the empty list.

Finally, the test cases are defined to verify the correctness of the function.