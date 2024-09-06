```python
def max_element(lst):
    return max(lst)

# Basic tests
assert(max_element([1, 2, 3]) == 3)
assert(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123)

# Edge case: empty list
assert(max_element([]) == [])

# Edge case: single element list
assert(max_element([5]) == 5)

# Test with negative numbers
assert(max_element([-5, 2, 3]) == -5)

# Test with list of different data types
assert(max_element([10, 20]) == 10)
assert(max_element([], type=int)) == None

# Test with custom data
my_list = [1, 2. + 3, 'abc', 4]
assert(max_element(my_list) == 4)
 ```