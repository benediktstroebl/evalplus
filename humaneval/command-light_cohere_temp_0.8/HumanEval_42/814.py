```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test case 1: Basic function call
test_incr_list = incr_list([1, 2, 3])
print("Test case 1: Result:", test_incr_list)

#Test case 2: List comprehension with built-in function call
test_incr_list2 = [i+1 for i in [5, 3, 5, 2, 3, 3, 9, 0, 123]]
print("Test case 2: Result:", test_incr_list2)

#Test case 3: List comprehension with generator expression
test_incr_list3 = list([6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
print("Test case 3: Result:", test_incr_list3)

#Test case 4: Nested list comprehension
test_incr_list4 = [a+1 for a in [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]]
print("Test case 4: Result:", test_incr_list4)

#Test case 5: Compound assignment list comprehension
test_incr_list5 = {key:value+1 for key, value in {'a':1, 'b':2, 'c':3}}.items()
print("Test case 5: Result:", test_incr_list5)
```