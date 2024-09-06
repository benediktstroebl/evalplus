```python
def triples_sum_to_zero(lst):
    if sum(map(lambda x: abs(x - y for x, y in zip(lst, lst[1:])))) == 0:
        return True
    return False

# Example usage:
if triples_sum_to_zero([1, 3, -2, 1]) == True:
    print("Success!")

if triples_sum_to_zero([1, 2, 3, 7]) == False:
    print("Failure.")

if triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True:
    print("Success.")

if triples_sum_to_zero([1]) == False:
    print("Failure.")
```
The function checks if there are three distinct elements in the list that their sum is equal to zero. If this is the condition is met, it returns True; otherwise, it returns False. 

It uses a lambda function to create a mapping that compares each element with the second element of the list, and checks if their absolute difference is non-zero, which indicates that the sum of these elements is not zero.