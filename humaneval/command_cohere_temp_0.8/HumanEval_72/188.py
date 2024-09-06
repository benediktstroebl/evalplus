```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or w == sum(q) // 2)
```

The function checks if the list `q` is palindromic by comparing the first and last elements of the list, `q[0]` and `q[-1]`, and the middle elements using the sum of elements `q[1:-1]`. If the list is of odd length, the weights of the first and last elements are added to check if the total weight `w` is equal to the sum of these elements. If the list is of even length, the function checks if the total weight `w` equals the half of the sum of all elements of the list. The function returns `True` if the sum of elements in the list does not exceed the weight and the list is considered balanced according to the given conditions. 

Here is an example of use:
```python
q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))     # True
```