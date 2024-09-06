```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies of length, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    l[:::2] = l[1::2] + [l[0]]
    return l
#Test cases
test_list = [1,2,3]
print("Test case 1 output: ",sort_even(test_list)) #[1,2,3]
test_list = [5,6,3,4]
print("Test case 2 output: ",sort_even(test_list)) # [3,6,5,4]
test_list = [3,6,5,4,1]
print("Test case 3 output: ",sort_even(test_list)) # [3,6,5,4,1]
```

The function `sort_even` takes a list `l` as input and returns a new list `l'` which is identical to `l` in the odd index of length, and its values at the even index are equal to the values of the even index of `l`, but sorted. 

The provided test cases will pass the output of the `sort_even` function to the console.