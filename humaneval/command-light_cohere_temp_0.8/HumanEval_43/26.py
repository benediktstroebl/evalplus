```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list has two distinct elements that sum to zero, False otherwise.
    """
    def sum_two_elements(x, y):
        return x + y == 0
    return sum_two_elements(l)

def sum_two_elements(list):
    if not defined(l):
        raise NameError("The list is empty")
    return sum(map(sum_two_elements, l))

if __name__ == "__main__":
    l = [1, 3, 5, 0]
    print(pairs_sum_to_zero(l))
    l = [1, 3, -2, 1]
    print(pairs_sum_to_zero(l))
    l = [1, 2, 3, 7]
    print(pairs_sum_to_zero(l))
    l = [2, 4, -5, 3, 5, 7]
    print(pairs_sum_to_zero(l))
```
This Python code defines a function `pairs_sum_to_zero` that checks if a given list contains two elements that sum to zero. It achieves this by creating a helper function `sum_two_elements` that checks if two elements in the list are equal and returns their sum. The `sum_two_elements` function iterates through the list and calculates the sum of all pairs of elements that result in a sum of zero. The `pairs_sum_to_zero` function then checks if the sum of the two elements is zero, which indicates the presence of two distinct elements that sum to zero. If the list is empty, a NameError is raised to handle the scenario.