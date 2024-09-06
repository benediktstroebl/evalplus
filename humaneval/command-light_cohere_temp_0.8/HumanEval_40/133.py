```python
def triples_sum_to_zero(lst):
    sum_to_zero = False
    for i in range(3):
        current_sum = sum(lst[i:])
        if current_sum < 0 and current_sum not in [0, lst[i], lst[(i+1) % len(lst)]) and sum_to_zero == False:
            sum_to_zero = True
            break
    return sum_to_zero

# Example usage
if __name__ == "__main__":
    lst = [1, 3, 5, 0]
    print(triples_sum_to_zero(lst))
``` 
This code defines a Python function `triples_sum_to_zero` that checks whether there are three distinct elements in a list that sum to zero. The function uses a simple algorithm to iterate through the list and checks if the sum of any three elements in the list will be zero. If the sum of any three elements is not zero, the function returns `False`, indicating that the condition is not met. If the sum of three elements is zero, the function returns `True`, indicating that the condition is met. 
The example usage demonstrates the function with a test list and prints the result. The output will be `True` or `False`, depending on whether the condition is met or not.