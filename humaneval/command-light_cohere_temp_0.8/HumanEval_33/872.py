```python
def sort_third(lst):
    return sorted(lst, key=lambda x: (x // 3) % 3)

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [15, 18, 10, 12],
    [23, 32, 33, 30]
]

for case in test_cases:
    print(sort_third(case))
``` 
This code defines a Python function `sort_third` that sorts a list using a custom key function that identifies and sorts numbers that are divisible by 3 and not. The list is then sorted according to this custom key, producing a list where numbers divisible by 3 maintain their original order and numbers not divisible by 3 are sorted to maintain their original order. 


Note that this function can be applied to any list of numbers, and it will produce a sorted list where numbers divisible by 3 are maintained in their original order and numbers not divisible by 3 are sorted to preserve their original order.