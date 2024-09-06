```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an argument. It returns a sorted list of all elements that do not have any even digits. The `not any()` function is used to check if there are any digits that are even in the string representation of each number. The `sorted()` function ensures the returned list is sorted in increasing order. 

The function basically screens each element in the input list `xs` to decide whether it ought to be remembered for the final list or not. Here, an element is acceptable if it doesn't have any even digits. To decide that, we loop over each digit in the string portrayal of the element (e.g., '1' for 1, '15' for 15, and so on) and check whether any of these digits is even - on the off chance that not, the element makes the cut. The subsequent list is sorted in increasing order, giving you the coveted result.