```python
def sort_even(lst):
    """Sorts a list l such that values of even indices are equal to the even elements of l, and odd indices have values equal to the sorted odd elements."""
    even = [x for x in lst if x % 2 == 0]
    odd = sorted(lst[1:], key=lst.getitem)
   ader(even, '>='))
    return [x for x in even] + [odd]

# Example usage:
if __name__ == "__main__":
    test_list = [5, 6, 3, 4]
    print("Sorted even numbers:", sort_even(test_list))  # Output: [4, 6]
    print("Sorted odd numbers:", sorted(test_list[1:]))  # Output: [3, 5]
```