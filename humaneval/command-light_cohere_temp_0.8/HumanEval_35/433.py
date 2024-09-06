```python
def max_element(lst):
    if not_elements(lst):
        return 0  # Return 0 for empty list
    return max(lst)

def not_elements(lst):
    if isinstance(lst, list) and len(lst) == 0:
        return False
    return all(isinstance(i, (int, float)) and i >= 0 for i in lst)

if __name__ == "__main__":
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
    print(max_element(['abc', 'def', 'ghi', 'jkl']))
    print(max_element([1234, 1235, 1236])))
    print(max_element([True, False, True]))
    print(max_element([{}]))
    print(max_element([[-123, -45], [123, 45], [12, 34]]))
```