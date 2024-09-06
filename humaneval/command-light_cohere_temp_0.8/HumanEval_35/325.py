```python
def max_element(lst):
    if not_elements(lst):  # Base case
        return None
    return max(lst, key=lambda x: x)

def not_elements(lst):
    return all(isinstance(x, (int, float)) and x >= 0 for x in lst)

# Unit tests
test_max_element = []
test_max_element.push(
    test_max_element.push((None))
test_max_element.push((max_element([1, 2, 3])) )
test_max_element.push((max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
test_max_element.push((max_element([5, 0, -5, -10, -20, 3, -100, -40, 0]))
test_max_element.push((max_element([123, 0, -123, -120]))
test_max_element.push(max_element([0, 0, 0]))
test_max_element.push(max_element([1, 2, -3, -10, -100]))

def main():
    test_max_element = []
    test_max_element.push(max_element([1, 2, 3, 4, 5]))
    print('Test Results:\n')
    print(' '.join(map(str, test_max_element)))

main()
```