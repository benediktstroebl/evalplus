```python
def pairs_sum_to_zero(lst):
    return any(x+y <= 0 for x, y in zip(lst, lst[1:])) and lst

# Example usage:
lst = [1, 3, 5, 0]
test_result = pairs_sum_to_zero(lst)
if test_result == True:
    print("pass")
else:
    print("fail")

```
This function checks whether two elements in the list are such that their sum equals zero, and returns the original list if true, or False otherwise.